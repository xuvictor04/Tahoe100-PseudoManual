---
symbol: "GSDMB"
type: "gene"
col: 1054
ensembl_id: "ENSG00000073605"
name: "gasdermin B"
location: "17q21.1"
module: 40
arm: "+"
pooled_cpm: 26.31
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 29
n_dd_up_clean: 12
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# GSDMB

*gasdermin B* — 17q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.55× (z +13.0, q 9e-36, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.284× (z -16.8, q 0e+00, down in 40 of 45 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.381× (z -13.4, q 2e-38, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ORMDL3]] (+0.76, fdr 7e-06, ⚠ same locus), [[PDXDC2P]] (+0.70, fdr 7e-06), [[PDXDC1]] (+0.67, fdr 7e-06), [[GAK]] (+0.67, fdr 1e-05); moves opposite to [[ZNF518A]] (-0.66, fdr 1e-05), [[CMTR2]] (-0.66, fdr 1e-05), [[METTL18]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SFTPA2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.55×** | +13.0 | 9e-36 | 40/46 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.29×** | +11.5 | 4e-28 | 36/46 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.16×** | +10.7 | 3e-24 | 35/45 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +7.0 | 5e-10 | 8/46 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +6.8 | 1e-09 | 28/46 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.5 | 4e-06 | 22/46 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +5.2 | 2e-05 | 23/45 (BT-474, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.003 | 21/43 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +3.7 | 0.015 | 16/46 (AsPC-1, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.017 | 11/45 (SNU-423, RKO, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.039 | 12/46 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.048 | 17/43 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.088 | 12/45 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.097 | 2/46 (HEC-1-A, A498) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1054.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.284×** | -16.8 | 0e+00 | 40/45 (NCI-H2030, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.381×** | -13.4 | 2e-38 | 37/45 (COLO 205, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.386×** | -13.2 | 2e-37 | 36/44 (HOP62, BT-474, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.524×** | -12.7 | 9e-35 | 36/45 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.401×** | -12.7 | 1e-34 | 37/46 (COLO 205, H4, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.410×** | -12.4 | 4e-33 | 35/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.484×** | -10.1 | 6e-22 | 34/45 (SW 900, SW480, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.336×** | -7.9 | 2e-13 | 35/46 (BT-474, COLO 205, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.349×** | -7.6 | 1e-12 | 33/42 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.604×** | -7.0 | 1e-10 | 29/45 (NCI-H1792, BT-474, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.708×** | -6.8 | 6e-10 | 31/46 (NCI-H1792, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.653×** | -5.9 | 2e-07 | 24/46 (SNU-1, A549, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.647×** | -5.8 | 3e-07 | 22/42 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.660×** | -5.8 | 3e-07 | 25/44 (SW480, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.666×** | -5.6 | 7e-07 | 29/45 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.732×** | -4.2 | 0.001 | 20/44 (PANC-1, HCT15, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.739×** | -4.0 | 0.002 | 20/45 (BT-474, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.764×** | -3.7 | 0.006 | 12/46 (A549, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.705×** | -3.5 | 0.015 | 14/45 (A549, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.621×** | -3.5 | 0.015 | 16/41 (NCI-H1792, Panc 03.27, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.623×** | -3.4 | 0.016 | 14/43 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.794×** | -3.2 | 0.033 | 12/46 (HCT15, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 149 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.60× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -16.4) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.363× (z -9.0) |
| [[PANC-1 (line)]] | alt | 11.2 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.71× (z +9.8) | [[Harringtonine (drug)]] 5 µM 0.187× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.272× (z -9.7) |
| [[SW480 (line)]] | alt | 28.2 | 1 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +8.7) | [[Harringtonine (drug)]] 0.5 µM 0.208× (z -12.7) |
| [[A498 (line)]] | wt | 63.9 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.153× (z -13.7) |
| [[COLO 205 (line)]] | alt | 140 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0641× (z -29.6) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -13.6) |
| [[LoVo (line)]] | wt | 45.6 | 2 (2 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.75× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Harringtonine (drug)]] 5 µM 0.253× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 24.3 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -13.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -9.1) |
| [[A549 (line)]] | wt | 13.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.9) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -11.4) |
| [[HT-29 (line)]] | alt | 32.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -16.0) ⚠ cell-cycle shift, explains ~61% of this change |
| [[KATO III (line)]] | alt | 41.1 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.52× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -14.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[Panc 03.27 (line)]] | alt | 35.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -18.7) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 40.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -15.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[HepG2_C3A (line)]] | wt | 32.6 | 0 | 3 (2 ⚠) | — | [[Roxadustat (drug)]] 0.05 µM 0.0652× (z -13.5) |
| [[HOP62 (line)]] | alt | 24.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.223× (z -10.3) |
| [[HS-578T (line)]] | alt | 23.3 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.155× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.159× (z -10.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.324× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 21.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.4) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 21.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -14.0) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -8.6) |
| [[H4 (line)]] | wt | 29.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0876× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.115× (z -9.2) |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.2) ⚠ cell-cycle shift, explains ~61% of this change |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.145× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 8.21 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.182× (z -9.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0835× (z -13.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 17.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.191× (z -9.7) |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 1 | — | [[Pimitespib (drug)]] 0.05 µM 0.0642× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 27.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.76× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0994× (z -9.9) |
| [[SNU-423 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -8.8) |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -13.8) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A-172 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.42 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.90 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORMDL3]] | +0.76 | +0.73 / +0.69 | both halves | 7e-06 | STRING 971; ⚠ same locus (1.2 kb, same strand: neighbours can correlate without regulation) |
| [[PDXDC2P]] | +0.70 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[GAK]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[GPR107]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PDXDC2P-NPIPB14P]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.66 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[WIPI1]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[BET1L]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[CYB561D2]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SLC31A1]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ARFGAP1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[PPP1R32]] | +0.62 | +0.64 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF518A]] | -0.66 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[CMTR2]] | -0.66 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[METTL18]] | -0.62 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[FAM169A]] | -0.60 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[MARCHF7]] | -0.60 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SLC16A9]] | -0.60 | -0.49 / -0.55 | both halves | 2e-05 |  |
| [[YTHDC2]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.58 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[SDSL]] | -0.58 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[MAPK1IP1L]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ZNF507]] | -0.57 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[SCAF8]] | -0.57 | -0.27 / -0.54 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFTPA2]] | C | SFTPA2 activity raises GSDMB's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 1.71× lower at baseline in the lines without SFTPA2 | 0.089 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.9, -31.8); signed map (-49.2, 9.9). **Vector** length 91.7, 23.0% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.4 | +10.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +13.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +11.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | +1.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.7 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +5.2 |
|  | [[Tolcapone (drug)]] 0.5 µM |  | +1.3 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.7 | -6.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -7.2 | -16.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -6.3 | -12.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.1 | -12.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -4.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -3.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | gasdermin B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.1 — chr17:39,904,595-39,919,854 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRO2521; previously GSDML |
| Gene groups (HGNC) | Gasdermins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAX9](https://www.uniprot.org/uniprotkb/Q8TAX9) (Gasdermin-B):

> [Gasdermin-B]: Precursor of a pore-forming protein that acts as a downstream mediator of granzyme-mediated cell death. This form constitutes the precursor of the pore-forming protein: upon cleavage, the released N-terminal moiety (Gasdermin-B, N-terminal) binds to membranes and forms pores, triggering pyroptosis. Also acts as a regulator of epithelial cell repair independently of programmed cell death: translocates to the plasma membrane and promotes epithelial maintenance and repair by …

**Summary**, from NCBI Gene [55876](https://www.ncbi.nlm.nih.gov/gene/55876):

> This gene encodes a member of the gasdermin-domain containing protein family. Other gasdermin-family genes are implicated in the regulation of apoptosis in epithelial cells, and are linked to cancer. Alternative splicing and the use of alternative promoters results in multiple transcript variants. Additional variants have been described, but they are candidates for nonsense-mediated mRNA decay (NMD) and are unlikely to be protein-coding. [provided by RefSeq, Nov 2016]

**Accessions** — [HGNC:23690](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23690) · Entrez [55876](https://www.ncbi.nlm.nih.gov/gene/55876) · UniProt [Q8TAX9](https://www.uniprot.org/uniprotkb/Q8TAX9) · Ensembl [ENSG00000073605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073605)

## Data

Gene col 1054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1054); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1054]; `tensor/DDL_lfc|DDL_z.npy` [1054]; `embed/gene_vectors.npy` [1054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1054 or target_col == 1054). Every well: [[GSDMB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSDMB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
