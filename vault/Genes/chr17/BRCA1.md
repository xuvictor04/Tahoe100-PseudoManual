---
symbol: "BRCA1"
type: "gene"
col: 250
ensembl_id: "ENSG00000012048"
name: "BRCA1 DNA repair associated"
location: "17q21.31"
module: 6
arm: "+"
pooled_cpm: 94.24
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# BRCA1

*BRCA1 DNA repair associated* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +13.2, q 6e-37, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.37× (z +7.9, q 6e-13, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.661× (z -7.3, q 1e-10, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZGRF1]] (+0.87, fdr 7e-06), [[ATAD5]] (+0.86, fdr 7e-06), [[FANCD2]] (+0.85, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TLCD3B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.70×** | +13.2 | 6e-37 | 36/47 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.86×** | +10.5 | 3e-23 | 32/42 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.81×** | +10.4 | 7e-23 | 38/48 (SNU-1, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.9 | 6e-13 | 32/47 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.51×** | +6.9 | 7e-10 | 30/47 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.49×** | +6.7 | 2e-09 | 33/49 (PANC-1, SW480, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.30×** | +6.5 | 7e-09 | 38/47 (SW480, SNU-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.38×** | +5.6 | 1e-06 | 30/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.37×** | +5.0 | 3e-05 | 24/44 (NCI-H2347, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.4 | 5e-04 | 24/47 (LoVo, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~90% of this change | **1.30×** | +4.4 | 6e-04 | 23/46 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.27×** | +4.2 | 0.001 | 21/47 (A-427, HT-29, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +4.1 | 0.001 | 25/47 (A549, LoVo, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.28×** | +4.1 | 0.001 | 26/47 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +4.1 | 0.002 | 22/47 (A549, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.005 | 19/47 (HS-578T, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.014 | 23/47 (HOP62, SW480, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.051 | 17/47 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.20×** | +3.0 | 0.069 | 18/47 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Aliskiren (drug)]] 5 µM |  | 1.13× | +2.9 | 0.076 | 3/48 (A-172, RPMI-7951, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.13× | +2.9 | 0.081 | 11/47 (NCI-H23, SHP-77, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +2.8 | 0.098 | 18/47 (PANC-1, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 250.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.661×** | -7.3 | 1e-10 | 30/47 (COLO 205, KATO III, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.454×** | -7.3 | 1e-10 | 42/47 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.770×** | -6.5 | 1e-08 | 35/47 (HOP62, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.705×** | -6.2 | 1e-07 | 36/47 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.797×** | -5.7 | 2e-06 | 25/47 (HEC-1-A, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.548×** | -5.5 | 3e-06 | 28/48 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.671×** | -5.0 | 4e-05 | 26/47 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.781×** | -4.4 | 9e-04 | 22/47 (A-172, A-427, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.847× | -4.2 | 0.002 | 22/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.806×** | -3.8 | 0.008 | 20/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.828×** | -3.3 | 0.042 | 18/47 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.876× | -3.3 | 0.042 | 19/47 (A498, A-427, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.822×** | -3.3 | 0.047 | 22/47 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.703×** | -3.2 | 0.047 | 18/44 (KATO III, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.836× | -3.2 | 0.056 | 21/47 (H4, A498, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.713×** | -3.1 | 0.065 | 23/47 (HEC-1-A, KATO III, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.70 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 210 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -12.0) |
| [[KATO III (line)]] | alt | 220 | 0 | 5 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.363× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.510× (z -10.9) |
| [[A549 (line)]] | wt | 73.1 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +13.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2347 (line)]] | alt | 40.3 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +11.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 82.0 | 3 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +10.4) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[A498 (line)]] | wt | 132 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.310× (z -14.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[COLO 205 (line)]] | alt | 115 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -10.6) |
| [[H4 (line)]] | wt | 82.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.273× (z -9.3) ⚠ cell-cycle shift, explains ~61% of this change |
| [[Hs 766T (line)]] | wt | 58.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -8.9) |
| [[HS-578T (line)]] | alt | 61.0 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +15.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[J82 (line)]] | alt | 136 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.1) ⚠ cell-cycle shift, explains ~67% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.491× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 76.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.34× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 104 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.221× (z -12.7) |
| [[RKO (line)]] | wt | 82.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.244× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~90% of this change |
| [[SW 1271 (line)]] | alt | 98.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0683× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.103× (z -9.6) |
| [[A-172 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.479× (z -9.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 160 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.461× (z -11.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HepG2_C3A (line)]] | wt | 38.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 45.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +10.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 64.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[NCI-H1792 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.41× (z +14.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 57.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 191 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.486× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 91.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +11.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[RPMI-7951 (line)]] | alt | 56.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +13.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.183× (z -8.5) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 50.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[SNU-423 (line)]] | alt | 85.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW 900 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 95.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW48 (line)]] | wt | 67.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[SW480 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +11.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 137 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZGRF1]] | +0.87 | +0.83 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[ATAD5]] | +0.86 | +0.83 / +0.86 | both halves | 7e-06 | STRING 691 |
| [[FANCD2]] | +0.85 | +0.85 / +0.84 | both halves | 7e-06 | same gene group; pathway: TP53 Regulates Transcription of DNA Repair Genes; STRING 999 |
| [[RAD51AP1]] | +0.85 | +0.79 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 854 |
| [[KNTC1]] | +0.83 | +0.83 / +0.78 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 849 |
| [[CHAF1A]] | +0.81 | +0.80 / +0.82 | both halves | 7e-06 | STRING 534 |
| [[FANCI]] | +0.81 | +0.76 / +0.87 | both halves | 7e-06 | same gene group; pathway: TP53 Regulates Transcription of DNA Repair Genes; STRING 993 |
| [[BRIP1]] | +0.81 | +0.81 / +0.84 | both halves | 7e-06 | same gene group; pathway: Cell Cycle Checkpoints; STRING 999 |
| [[GINS1]] | +0.80 | +0.80 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 469 |
| [[POLQ]] | +0.80 | +0.82 / +0.83 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 751 |
| [[RRM1]] | +0.80 | +0.75 / +0.82 | both halves | 7e-06 | STRING 652 |
| [[DNA2]] | +0.79 | +0.78 / +0.79 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 897 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLCD3B]] | B | TLCD3B activity raises BRCA1's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.15× lower at baseline in the lines without TLCD3B | 0.014 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers BRCA1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM111B]] | B | FAM111B activity raises BRCA1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.40× lower at baseline in the lines without FAM111B | 0.069 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[C21orf58]], [[CDC45]], [[CENPM]], [[SKA3]] | C | C21orf58, CDC45, CENPM, SKA3 activity raises BRCA1's level | lines that do not express C21orf58, CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.60× lower at baseline in the lines without C21orf58, CDC45, CENPM (+1 more) | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[E2F1]] | C | E2F1 activity raises BRCA1's level | lines that do not express E2F1 (3) vs lines expressing it (47) | 2.48× lower at baseline in the lines without E2F1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |
| [[MYBL2]] | C | MYBL2 activity raises BRCA1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.31× lower at baseline in the lines without MYBL2 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |
| [[CLSPN]] | C | CLSPN activity raises BRCA1's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 1.86× lower at baseline in the lines without CLSPN | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |
| [[MCM2]] | C | MCM2 activity raises BRCA1's level | lines that do not express MCM2 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without MCM2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRC20, SEMA3F, CDC45; maybe low, not absent; its own permutation p |
| [[MCM10]] | C | MCM10 activity raises BRCA1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.16× lower at baseline in the lines without MCM10 | 0.0997 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.788). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.9, -46.3); signed map (-40.9, -47.2). **Vector** length 137, 48.6% of its response variance represented; |z| ≥ 3 in 1,317 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.65 to 28); *DNA Replication* (reactome, mean cos +0.64 to 40); *E2F G1/S* (control, mean cos +0.63 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +5.7 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +5.2 | +5.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +4.6 | +6.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +4.6 | +4.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +4.2 | +3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +3.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.4 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +2.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.9 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -11.3 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -8.4 | -6.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -7.5 | -3.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -5.3 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -7.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -4.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.8 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.7 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | BRCA1 DNA repair associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,044,295-43,170,245 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF53, BRCC1, PPP1R53, FANCS |
| Gene groups (HGNC) | Ring finger proteins; FA complementation groups; Protein phosphatase 1 regulatory subunits; BRCA1 A complex; BRCA1 B complex; BRCA1 C complex |
| Hallmark sets | APICAL_SURFACE, ALLOGRAFT_REJECTION, APOPTOSIS, E2F_TARGETS |
| Reactome | 51 pathways, smallest: Regulation of MITF-M-dependent genes involved in DNA replication, damage repair and senescence; Impaired BRCA2 binding to PALB2; Metalloprotease DUBs |
| Matched by | ensembl_id |

**Function**, from UniProt [P38398](https://www.uniprot.org/uniprotkb/P38398) (Breast cancer type 1 susceptibility protein):

> E3 ubiquitin-protein ligase that specifically mediates the formation of 'Lys-6'-linked polyubiquitin chains and plays a central role in DNA repair by facilitating cellular responses to DNA damage. It is unclear whether it also mediates the formation of other types of polyubiquitin chains. The BRCA1-BARD1 heterodimer coordinates a diverse range of cellular pathways such as DNA damage repair, ubiquitination and transcriptional regulation to maintain genomic stability. Regulates centrosomal …

**Summary**, from NCBI Gene [672](https://www.ncbi.nlm.nih.gov/gene/672):

> This gene encodes a 190 kD nuclear phosphoprotein that plays a role in maintaining genomic stability, and it also acts as a tumor suppressor. The BRCA1 gene contains 22 exons spanning about 110 kb of DNA. The encoded protein combines with other tumor suppressors, DNA damage sensors, and signal transducers to form a large multi-subunit protein complex known as the BRCA1-associated genome surveillance complex (BASC). This gene product associates with RNA polymerase II, and through the C-terminal …

**Accessions** — [HGNC:1100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1100) · Entrez [672](https://www.ncbi.nlm.nih.gov/gene/672) · UniProt [P38398](https://www.uniprot.org/uniprotkb/P38398) · Ensembl [ENSG00000012048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012048)

## Data

Gene col 250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 250); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 250]; `tensor/DDL_lfc|DDL_z.npy` [250]; `embed/gene_vectors.npy` [250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 250 or target_col == 250). Every well: [[BRCA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRCA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
