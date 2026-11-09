---
symbol: "HMGB3"
type: "gene"
col: 394
ensembl_id: "ENSG00000029993"
name: "high mobility group box 3"
location: "Xq28"
module: 22
arm: "+"
pooled_cpm: 36.37
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# HMGB3

*high mobility group box 3* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.74× (z +17.8, q 0e+00, up in 40 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +9.3, q 2e-18, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.582× (z -5.9, q 3e-06, down in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[Artesunate (drug)]] 0.5 µM: 0.745× (z -3.4, q 0.069, down in 12 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 10 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SHP-77 0.186×, A-427 0.135×, SW 900 0.377×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.175×, A-427 0.413×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SHP-77 0.243×, SW 900 0.230×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KPNA2]] (+0.72, fdr 7e-06), [[ARHGAP11A]] (+0.71, fdr 7e-06), [[PRC1]] (+0.70, fdr 7e-06); moves opposite to [[DUXAP10]] (-0.53, fdr 3e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 394.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.74×** | +17.8 | 0e+00 | 40/41 (A-172, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.99×** | +15.2 | 0e+00 | 33/35 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +10.7 | 3e-24 | 35/41 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +9.3 | 2e-18 | 35/46 (A498, A549, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.95×** | +7.7 | 2e-12 | 38/44 (HOP62, HT-29, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +5.8 | 7e-07 | 27/42 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.8 | 1e-04 | 5/47 (SW 900, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +4.4 | 8e-04 | 24/46 (NCI-H1792, COLO 205, …) | top dose only | composition shift; position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.45×** | +4.3 | 0.001 | 24/46 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.31×** | +4.2 | 0.002 | 22/47 (NCI-H2030, A549, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.003 | 26/47 (A-427, SW480, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.38×** | +3.7 | 0.011 | 19/46 (HOP62, NCI-H460, …) | two highest doses | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.015 | 22/46 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~74% of this change | **1.38×** | +3.6 | 0.015 | 23/46 (NCI-H1573, A-172, …) | top dose only |  |
| [[Allantoin (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.026 | 14/47 (SHP-77, SW480, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.054 | 20/46 (CFPAC-1, NCI-H1573, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.30×** | +3.0 | 0.085 | 15/47 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.31×** | +2.9 | 0.093 | 11/47 (PANC-1, A549, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.093 | 14/47 (HT-29, CFPAC-1, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 394.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 10 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SHP-77 0.186×, A-427 0.135×, SW 900 0.377×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.175×, A-427 0.413×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SHP-77 0.243×, SW 900 0.230×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.582×** | -5.9 | 3e-06 | 32/47 (SHP-77, SW 900, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.734×** | -4.8 | 6e-04 | 28/47 (SW480, COLO 205, …) | rises with dose | position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.688×** | -4.1 | 0.007 | 26/46 (BT-474, SW 1271, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.705×** | -4.0 | 0.009 | 23/47 (CHP-212, HT-29, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.730×** | -3.6 | 0.035 | 21/46 (SW 900, SHP-77, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.745×** | -3.4 | 0.069 | 12/47 (H4, LS 180, …) | rises with dose | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.763× | -3.1 | 0.13 | 14/46 (A549, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.824× | -3.0 | 0.13 | 18/47 (MIA PaCa-2, A-172, …) | all doses, flat | low cells (technical?) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.689× | -3.0 | 0.13 | 11/47 (A-427, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.768× | -3.0 | 0.13 | 18/46 (HEC-1-A, RKO, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.823× | -3.0 | 0.13 | 18/47 (SHP-77, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 285 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -18.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -17.9) |
| [[SW 900 (line)]] | alt | 163 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.171× (z -11.4) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -8.6) |
| [[A-172 (line)]] | wt | 33.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.50× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 44.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -14.7) |
| [[A498 (line)]] | wt | 17.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +12.0) | — |
| [[A549 (line)]] | wt | 36.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.41× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 24.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[KATO III (line)]] | alt | 34.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.71× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 23.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.61× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Selinexor (drug)]] 5 µM 0.332× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 24.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 28.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 32.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 22.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 64.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SNU-423 (line)]] | alt | 23.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C-33 A (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LS 180 (line)]] | wt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.19× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 76.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 39.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW48 (line)]] | wt | 29.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 38.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.43 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA2]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ARHGAP11A]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[PRC1]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CCNB1]] | +0.70 | +0.65 / +0.73 | both halves | 7e-06 | STRING 428 |
| [[ASPM]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[MKI67]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[HP1BP3]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[KIF20A]] | +0.68 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[DEPDC1]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CENPF]] | +0.68 | +0.72 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[TPX2]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[KNSTRN]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUXAP10]] | -0.53 | -0.51 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises HMGB3's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.0, -55.4); signed map (-51.0, -44.6). **Vector** length 98.5, 26.6% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.62 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.53 to 48); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.53 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +6.0 | +17.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.9 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +5.7 | +15.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +9.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | +4.7 | +7.7 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.1 | +0.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +2.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | -5.0 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -4.9 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -2.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.5 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group box 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:150,980,509-150,990,771 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HMG2A, MGC90319; previously HMG4 |
| Gene groups (HGNC) | Canonical high mobility group |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [O15347](https://www.uniprot.org/uniprotkb/O15347) (High mobility group protein B3):

> Multifunctional protein with various roles in different cellular compartments. May act in a redox sensitive manner. Associates with chromatin and binds DNA with a preference for non-canonical DNA structures such as single-stranded DNA. Can bend DNA and enhance DNA flexibility by looping thus providing a mechanism to promote activities on various gene promoters (By similarity). Proposed to be involved in the innate immune response to nucleic acids by acting as a cytoplasmic promiscuous …

**Summary**, from NCBI Gene [3149](https://www.ncbi.nlm.nih.gov/gene/3149):

> This gene encodes a member of a family of proteins containing one or more high mobility group DNA-binding motifs. The encoded protein plays an important role in maintaining stem cell populations, and may be aberrantly expressed in tumor cells. A mutation in this gene was associated with microphthalmia, syndromic 13. There are numerous pseudogenes of this gene on multiple chromosomes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:5004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5004) · Entrez [3149](https://www.ncbi.nlm.nih.gov/gene/3149) · UniProt [O15347](https://www.uniprot.org/uniprotkb/O15347) · Ensembl [ENSG00000029993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000029993)

## Data

Gene col 394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 394); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 394]; `tensor/DDL_lfc|DDL_z.npy` [394]; `embed/gene_vectors.npy` [394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 394 or target_col == 394). Every well: [[HMGB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
