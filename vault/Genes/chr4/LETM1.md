---
symbol: "LETM1"
type: "gene"
col: 9725
ensembl_id: "ENSG00000168924"
name: "leucine zipper and EF-hand containing transmembrane protein 1"
location: "4p16.3"
module: 18
arm: "+"
pooled_cpm: 22.93
n_lines_expressing: 50
n_dd_up: 51
n_dd_down: 5
n_dd_up_clean: 26
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# LETM1

*leucine zipper and EF-hand containing transmembrane protein 1* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 51 drug-doses (25 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.05× (z +15.9, q 0e+00, up in 43 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.69× (z +7.4, q 9e-12, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.789× (z -4.8, q 8e-04, down in 22 of 48 measured lines) ⚠ cell-cycle shift, explains ~69% of this change. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 0.755× (z -3.9, q 0.020, down in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (RKO 0.290×, J82 0.420×, SW48 0.385×; ⚠ cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.0911×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.287×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.115×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.119×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.84, fdr 7e-06), [[PUS1]] (+0.82, fdr 7e-06), [[CTPS1]] (+0.81, fdr 7e-06); moves opposite to [[CCNG2]] (-0.67, fdr 7e-06), [[AAMDC]] (-0.64, fdr 7e-06), [[AFTPH]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 27 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 51 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.05×** | +15.9 | 0e+00 | 43/45 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.97×** | +14.9 | 0e+00 | 31/35 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.29×** | +10.9 | 2e-25 | 37/43 (NCI-H23, SW480, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.94×** | +9.5 | 4e-19 | 38/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.99×** | +9.4 | 5e-19 | 37/47 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +7.4 | 9e-12 | 30/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +7.2 | 6e-11 | 31/44 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +6.4 | 9e-09 | 27/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.54×** | +6.1 | 6e-08 | 22/46 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.51×** | +5.8 | 3e-07 | 25/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.51×** | +5.6 | 1e-06 | 25/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.5 | 2e-06 | 26/46 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.47×** | +5.5 | 2e-06 | 25/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.07×** | +5.4 | 3e-06 | 27/47 (NCI-H460, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.45×** | +5.3 | 4e-06 | 24/45 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +5.1 | 1e-05 | 20/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.1 | 1e-05 | 27/47 (SW480, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.0 | 2e-05 | 23/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +5.0 | 2e-05 | 23/47 (C32, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.88×** | +4.7 | 6e-05 | 23/47 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.86×** | +4.6 | 9e-05 | 21/44 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.82×** | +4.5 | 2e-04 | 22/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +4.4 | 2e-04 | 18/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 3e-04 | 20/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 3e-04 | 21/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9725.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (RKO 0.290×, J82 0.420×, SW48 0.385×; ⚠ cell-cycle shift, would explain all of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.0911×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.287×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.115×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.789×** | -4.8 | 8e-04 | 22/48 (A498, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.725×** | -4.6 | 0.001 | 21/47 (A-427, A498, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.755×** | -3.9 | 0.020 | 21/47 (HepG2/C3A, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.768×** | -3.8 | 0.021 | 22/47 (CHP-212, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -3.7 | 0.025 | 17/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.780×** | -3.6 | 0.033 | 13/48 (AsPC-1, H4, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.803× | -3.2 | 0.12 | 17/48 (LoVo, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.806× | -3.1 | 0.13 | 10/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.802× | -3.0 | 0.14 | 10/47 (A549, SNU-423, …) | top dose only | plate-row cell shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.809× | -3.0 | 0.15 | 10/47 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 23.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.490× (z -8.6) ⚠ cell-cycle shift, explains ~69% of this change |
| [[MIA PaCa-2 (line)]] | alt | 24.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.29× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Adagrasib (drug)]] 0.05 µM 0.659× (z -9.0) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 12.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.21× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.65× (z +8.7) | — |
| [[RKO (line)]] | wt | 49.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -14.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -10.4) |
| [[SW480 (line)]] | alt | 26.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.115× (z -9.8) |
| [[J82 (line)]] | alt | 38.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 30.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 22.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 49.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.49× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[Hs 766T (line)]] | wt | 12.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.62× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HT-29 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[KATO III (line)]] | alt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LS 180 (line)]] | wt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H23 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.58× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SHP-77 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.204× (z -8.9) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0911× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 8.88 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.78× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW48 (line)]] | wt | 56.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.84 | +0.80 / +0.85 | both halves | 7e-06 |  |
| [[PUS1]] | +0.82 | +0.78 / +0.82 | both halves | 7e-06 |  |
| [[CTPS1]] | +0.81 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[WDR77]] | +0.79 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.79 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.79 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[URB2]] | +0.78 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.78 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.77 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[PGAM5]] | +0.77 | +0.78 / +0.76 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[BOP1]] | +0.76 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[PINX1]] | +0.75 | +0.70 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNG2]] | -0.67 | -0.64 / -0.71 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.64 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[AFTPH]] | -0.64 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[SIRT2]] | -0.63 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[DBP]] | -0.63 | -0.56 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises LETM1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without ADCY3 | 0.056 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[WNK2]] | B | WNK2 activity raises LETM1's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.49× lower at baseline in the lines without WNK2 | 0.094 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.805). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-12.7, -36.5); signed map (-3.2, -48.9). **Vector** length 93.9, 24.6% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.9 | +9.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.0 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +3.9 | +15.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +3.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -4.2 | -4.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -3.6 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.1 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.8 | -3.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | leucine zipper and EF-hand containing transmembrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,811,479-1,856,156 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLC55A1, Mdm38 |
| Gene groups (HGNC) | EF-hand domain containing; Solute carrier family 55, LETM mitochondrial cation/proton exchangers |
| Reactome | 9 pathways, smallest: Mitochondrial calcium ion transport; Complex III assembly; RHOG GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O95202](https://www.uniprot.org/uniprotkb/O95202) (Mitochondrial proton/calcium exchanger protein):

> Plays an important role in maintenance of mitochondrial morphology and in mediating either calcium or potassium/proton antiport. Mediates proton-dependent calcium efflux from mitochondrion. Also functions as an electroneutral mitochondrial proton/potassium exchanger. Crucial for the maintenance of mitochondrial tubular networks and for the assembly of the supercomplexes of the respiratory chain. Required for the maintenance of the tubular shape and cristae organization.

**Summary**, from NCBI Gene [3954](https://www.ncbi.nlm.nih.gov/gene/3954):

> This gene encodes a protein that is localized to the inner mitochondrial membrane. The protein functions to maintain the mitochondrial tubular shapes and is required for normal mitochondrial morphology and cellular viability. Mutations in this gene cause Wolf-Hirschhorn syndrome, a complex malformation syndrome caused by the deletion of parts of the distal short arm of chromosome 4. Related pseudogenes have been identified on chromosomes 8, 15 and 19. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:6556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6556) · Entrez [3954](https://www.ncbi.nlm.nih.gov/gene/3954) · UniProt [O95202](https://www.uniprot.org/uniprotkb/O95202) · Ensembl [ENSG00000168924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168924)

## Data

Gene col 9725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9725); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9725]; `tensor/DDL_lfc|DDL_z.npy` [9725]; `embed/gene_vectors.npy` [9725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9725 or target_col == 9725). Every well: [[LETM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LETM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
