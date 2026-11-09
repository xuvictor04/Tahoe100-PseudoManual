---
symbol: "CRYBG3"
type: "gene"
col: 1276
ensembl_id: "ENSG00000080200"
name: "crystallin beta-gamma domain containing 3"
location: "3q11.2"
module: 180
arm: "+"
pooled_cpm: 132.22
n_lines_expressing: 47
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# CRYBG3

*crystallin beta-gamma domain containing 3* — 3q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.36× (z +6.1, q 7e-07, up in 31 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.23× (z +4.0, q 0.015, up in 23 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 2.65×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 1 line (A-427 2.19×; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 1.90×; ⚠ cell-cycle shift, explains ~19% of this change).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.397× (z -17.6, q 0e+00, down in 37 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.574× (z -5.8, q 4e-07, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARFGEF3]] (+0.71, fdr 7e-06), [[BNIP3]] (+0.65, fdr 1e-05), [[C1GALT1]] (+0.62, fdr 7e-06); moves opposite to [[AKT2]] (-0.47, fdr 6e-05), [[RAD51-AS1]] (-0.46, fdr 3e-04), [[ASPSCR1]] (-0.45, fdr 6e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DTNA]] → it (grade B ⚠); 4 go from it, the strongest it → [[DTNA]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1276.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 2.65×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 1 line (A-427 2.19×; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 1.90×; ⚠ cell-cycle shift, explains ~19% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +6.1 | 7e-07 | 31/45 (SW 900, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.015 | 23/44 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.071 | 25/45 (HOP62, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | 1.18× | +3.1 | 0.23 | 19/45 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | 1.34× | +3.1 | 0.23 | 18/45 (LoVo, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 24 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1276.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -17.6 | 0e+00 | 37/41 (A549, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.434×** | -16.6 | 0e+00 | 41/46 (J82, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.494×** | -13.5 | 5e-39 | 40/44 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.483×** | -13.3 | 2e-38 | 37/42 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.636×** | -12.7 | 8e-35 | 30/45 (A-172, SNU-423, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.587×** | -10.6 | 4e-24 | 38/45 (SNU-423, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.636×** | -9.0 | 3e-17 | 33/45 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.638×** | -8.6 | 8e-16 | 39/44 (J82, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.682×** | -7.3 | 2e-11 | 29/45 (A-172, NCI-H460, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.774×** | -7.2 | 4e-11 | 28/46 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.727×** | -6.3 | 2e-08 | 27/45 (SNU-423, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.745×** | -5.8 | 3e-07 | 29/45 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.574×** | -5.8 | 4e-07 | 31/46 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.751×** | -5.7 | 6e-07 | 29/45 (C32, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.754×** | -5.6 | 8e-07 | 31/45 (C32, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -5.5 | 1e-06 | 30/45 (SK-MEL-2, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.847× | -4.6 | 1e-04 | 21/45 (HOP62, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.668×** | -4.2 | 7e-04 | 23/45 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.778×** | -3.5 | 0.009 | 25/45 (CFPAC-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.844× | -3.2 | 0.026 | 18/45 (NCI-H1792, C32, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.867× | -2.8 | 0.088 | 17/45 (NCI-H23, SHP-77, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 115 | 0 | 15 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -18.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.355× (z -12.9) |
| [[J82 (line)]] | alt | 232 | 0 | 13 (13 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 261 | 0 | 12 (9 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.266× (z -14.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.311× (z -13.3) |
| [[SNU-423 (line)]] | alt | 219 | 0 | 12 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -21.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 195 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -27.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.558× (z -9.4) |
| [[HOP62 (line)]] | alt | 170 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.582× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 178 | 0 | 10 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 257 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -23.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.389× (z -12.8) |
| [[HS-578T (line)]] | alt | 174 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -18.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 160 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.148× (z -12.0) |
| [[A549 (line)]] | wt | 108 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0982× (z -28.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 162 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.457× (z -10.1) |
| [[LoVo (line)]] | wt | 110 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.294× (z -9.6) |
| [[LS 180 (line)]] | wt | 81.6 | 3 (3 ⚠) | 2 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.443× (z -8.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 205 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -21.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 146 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 147 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -13.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 179 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -11.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 123 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 165 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 158 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0922× (z -15.2) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 211 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -15.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 123 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +10.3) ⚠ cell-cycle shift, explains ~51% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -12.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 145 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -10.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 146 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.400× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 169 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.495× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 148 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -18.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 91.8 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.353× (z -10.1) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 173 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 123 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.209× (z -19.7) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 175 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0876× (z -24.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 72.3 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -12.1) ⚠ cell-cycle shift, explains ~19% of this change |
| [[COLO 205 (line)]] | alt | 96.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.0) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 80.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 97.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.474× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 116 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 75.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.484× (z -10.6) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -9.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 67.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.500× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 30.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGEF3]] | +0.71 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[BNIP3]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[C1GALT1]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[YEATS2]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TBC1D9B]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[GRPEL1]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PPFIA4]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[INTS13]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PLAAT1]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[NGLY1]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CCDC47]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[USP28]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT2]] | -0.47 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[RAD51-AS1]] | -0.46 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[ASPSCR1]] | -0.45 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[ATG13]] | -0.43 | -0.21 / -0.49 | both halves | 6e-04 |  |
| [[FOXK1]] | -0.43 | -0.29 / -0.56 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DTNA]] | B | DTNA activity raises CRYBG3's level | lines that do not express DTNA (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without DTNA | 0.007 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |
| [[ZNF215]] | B | ZNF215 activity raises CRYBG3's level | lines that do not express ZNF215 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without ZNF215 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000283415, ENSG00000291143 |
| [[MLLT3]] | B | MLLT3 activity raises CRYBG3's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without MLLT3 | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[PAM]] | C | PAM activity raises CRYBG3's level | lines that do not express PAM (3) vs lines expressing it (47) | 5.15× lower at baseline in the lines without PAM | 2e-04 | ⚠ few lines (3 vs 47); across organs; also absent: PARP3, OSBPL3, CRYBG3; maybe low, not absent; co-absent with the target |
| [[PFKP]] | C | PFKP activity raises CRYBG3's level | lines that do not express PFKP (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without PFKP | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DTNA]] | C | CRYBG3 activity raises DTNA's level | lines that do not express CRYBG3 (3) vs lines expressing it (47) | 4.36× lower at baseline in the lines without CRYBG3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPR137B, PAM, DTX3L; its own permutation p |
| [[NGLY1]] | C | CRYBG3 activity raises NGLY1's level | lines that do not express CRYBG3 (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without CRYBG3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPR137B, PAM, DTX3L |
| [[EIF4A3]] | C | CRYBG3 activity lowers EIF4A3's level | lines that do not express CRYBG3 (3) vs lines expressing it (47) | 1.72× higher at baseline in the lines without CRYBG3 | 0.082 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPR137B, PAM, DTX3L |
| [[DIPK2A]] | C | CRYBG3 activity raises DIPK2A's level | lines that do not express CRYBG3 (3) vs lines expressing it (47) | 2.67× lower at baseline in the lines without CRYBG3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPR137B, PAM, DTX3L; its own permutation p |

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.7, -17.0); signed map (-38.0, 26.1). **Vector** length 111, 36.5% of its response variance represented; |z| ≥ 3 in 1,267 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.2 | +6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.9 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.8 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.8 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.8 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.0 | +1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.8 | +2.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.5 | -13.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -3.8 | -10.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.3 | -13.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | crystallin beta-gamma domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q11.2 — chr3:97,822,011-97,944,984 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp667G2110 |
| Gene groups (HGNC) | Beta-gamma crystallin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68DQ2](https://www.uniprot.org/uniprotkb/Q68DQ2) (Very large A-kinase anchor protein):

> [Isoform vlAKAP]: Anchoring protein that mediates the subcellular compartmentation of protein kinase A (PKA).

**Summary**, from NCBI Gene [131544](https://www.ncbi.nlm.nih.gov/gene/131544):

> Enables protein kinase A binding activity. Predicted to be involved in lens development in camera-type eye and visual perception. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34427) · Entrez [131544](https://www.ncbi.nlm.nih.gov/gene/131544) · UniProt [Q68DQ2](https://www.uniprot.org/uniprotkb/Q68DQ2) · Ensembl [ENSG00000080200](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080200)

## Data

Gene col 1276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1276); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1276]; `tensor/DDL_lfc|DDL_z.npy` [1276]; `embed/gene_vectors.npy` [1276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1276 or target_col == 1276). Every well: [[CRYBG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRYBG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
