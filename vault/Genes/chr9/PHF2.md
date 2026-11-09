---
symbol: "PHF2"
type: "gene"
col: 12448
ensembl_id: "ENSG00000197724"
name: "PHD finger protein 2"
location: "9q22.31"
module: 46
arm: "+"
pooled_cpm: 33.96
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# PHF2

*PHD finger protein 2* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.11× (z +7.9, q 2e-12, up in 2 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.27× (z +7.3, q 8e-11, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.190× (z -35.6, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRD1]] (+0.76, fdr 7e-06), [[SETD1B]] (+0.73, fdr 2e-05), [[UBTF]] (+0.72, fdr 1e-05); moves opposite to [[RADX]] (-0.58, fdr 1e-04), [[CDK18]] (-0.56, fdr 9e-05), [[TMEM14A]] (-0.55, fdr 4e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARHGEF35-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12448.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +7.9 | 2e-12 | 2/48 (NCI-H1573, NCI-H23) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +7.3 | 8e-11 | 26/48 (MIA PaCa-2, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 0.002 | 15/48 (NCI-H1792, RKO, …) | inconsistent across doses | position effect removed |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 0.002 | 12/48 (HCT15, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.003 | 12/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.003 | 16/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.1 | 0.15 | 8/48 (MIA PaCa-2, SNU-423, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.17 | 9/47 (SW48, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12448.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.190×** | -35.6 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.202×** | -34.3 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.229×** | -31.6 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.428×** | -18.2 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.633×** | -13.9 | 1e-41 | 46/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.593×** | -11.2 | 4e-27 | 38/47 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.627×** | -10.0 | 1e-21 | 36/48 (C32, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.424×** | -9.6 | 5e-20 | 38/48 (SW480, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.596×** | -5.8 | 4e-07 | 24/48 (Panc 03.27, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.604×** | -5.7 | 9e-07 | 23/49 (PANC-1, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.779×** | -5.4 | 4e-06 | 22/48 (HT-29, LOX-IMVI, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.847× | -3.4 | 0.027 | 20/48 (SW 900, SK-MEL-2, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.894× | -3.4 | 0.030 | 15/48 (A-172, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.859× | -3.3 | 0.043 | 14/48 (NCI-H23, NCI-H1573, …) | two highest doses | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | 0.860× | -3.2 | 0.043 | 8/47 (NCI-H2347, NCI-H661, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.866× | -3.1 | 0.067 | 9/48 (A549, A498, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 37.6 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -19.4) |
| [[NCI-H460 (line)]] | wt | 44.4 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -27.6) |
| [[J82 (line)]] | alt | 51.5 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -23.2) |
| [[RKO (line)]] | wt | 55.4 | 1 | 5 | [[Auranofin (drug)]] 5 µM 2.54× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -16.2) |
| [[SW480 (line)]] | alt | 39.3 | 1 | 5 | [[Auranofin (drug)]] 5 µM 2.23× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -26.1) |
| [[A-172 (line)]] | wt | 37.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.202× (z -14.2) |
| [[C32 (line)]] | wt | 35.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -17.0) |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -16.2) |
| [[HT-29 (line)]] | alt | 30.5 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.111× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 41.6 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -17.9) |
| [[SHP-77 (line)]] | alt | 26.7 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -13.8) |
| [[SW1417 (line)]] | alt | 45.0 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -18.7) |
| [[C-33 A (line)]] | alt | 54.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 59.2 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.39× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -17.5) |
| [[HOP62 (line)]] | alt | 34.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -16.4) |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -12.6) |
| [[KATO III (line)]] | alt | 37.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0980× (z -21.2) |
| [[LoVo (line)]] | wt | 37.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0989× (z -24.7) |
| [[MIA PaCa-2 (line)]] | alt | 30.5 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -18.7) |
| [[NCI-H2347 (line)]] | alt | 27.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -15.9) |
| [[SK-MEL-2 (line)]] | alt | 26.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.05 µM 0.195× (z -11.6) |
| [[SNU-423 (line)]] | alt | 33.8 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.185× (z -14.3) |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -11.5) |
| [[A498 (line)]] | wt | 34.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -13.9) |
| [[A549 (line)]] | wt | 33.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -16.5) |
| [[AsPC-1 (line)]] | alt | 17.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -14.0) |
| [[COLO 205 (line)]] | alt | 28.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -13.7) |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 53.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.143× (z -13.3) |
| [[LS 180 (line)]] | wt | 38.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.158× (z -18.4) |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.186× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 25.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 30.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 20.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -14.4) |
| [[PANC-1 (line)]] | alt | 19.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.317× (z -11.0) |
| [[SNU-1 (line)]] | wt | 50.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -13.0) |
| [[SW48 (line)]] | wt | 49.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -13.4) |
| [[A-427 (line)]] | wt | 21.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -9.3) |
| [[AN3 CA (line)]] | alt | 66.9 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0874× (z -12.3) |
| [[H4 (line)]] | wt | 20.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -9.6) |
| [[BT-474 (line)]] | alt | 29.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 25.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -12.1) |
| [[SW 1271 (line)]] | alt | 62.7 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.111× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD1]] | +0.76 | +0.60 / +0.69 | both halves | 7e-06 | same gene group; pathway: Chromatin modifying enzymes |
| [[SETD1B]] | +0.73 | +0.47 / +0.67 | both halves | 2e-05 | pathway: Chromatin modifying enzymes; STRING 460 |
| [[UBTF]] | +0.72 | +0.53 / +0.62 | both halves | 1e-05 | same gene group |
| [[DNMT3A]] | +0.70 | +0.63 / +0.58 | both halves | 7e-06 | same gene group; pathway: Chromatin modifying enzymes |
| [[PHF8]] | +0.66 | +0.40 / +0.60 | both halves | 5e-05 | same gene group; pathway: Chromatin modifying enzymes; STRING 512 |
| [[EFCAB2]] | +0.65 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[STRN4]] | +0.64 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[PRDM11]] | +0.62 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[ZNF362]] | +0.61 | +0.40 / +0.47 | both halves | 4e-05 |  |
| [[ZMYND11]] | +0.61 | +0.45 / +0.48 | both halves | 3e-05 | same gene group |
| [[MYLK4]] | +0.61 | +0.26 / +0.48 | both halves | 4e-04 |  |
| [[PRDM5]] | +0.61 | +0.34 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RADX]] | -0.58 | -0.36 / -0.51 | both halves | 1e-04 | same gene group |
| [[CDK18]] | -0.56 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[TMEM14A]] | -0.55 | -0.25 / -0.54 | both halves | 4e-04 |  |
| [[FRRS1]] | -0.55 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[EDA]] | -0.54 | -0.43 / -0.37 | both halves | 8e-05 | same gene group |
| [[PAFAH1B3]] | -0.54 | -0.16 / -0.33 | ⚠ not reproduced | 0.001 |  |
| [[NME7]] | -0.54 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[GDE1]] | -0.53 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[EFHC1]] | -0.52 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[PELO]] | -0.52 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[GPR160]] | -0.52 | -0.34 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF35-AS1]] | B | ARHGEF35-AS1 activity lowers PHF2's level | lines that do not express ARHGEF35-AS1 (13) vs lines expressing it (37) | 1.36× higher at baseline in the lines without ARHGEF35-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ARHGEF5, MCTP2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PHF2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises PHF2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.6, 12.1); signed map (25.9, -24.8). **Vector** length 100, 24.3% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.1 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.3 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.1 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.2 | -13.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.8 | -10.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.7 | -18.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.0 | -31.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -34.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | -9.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -2.2 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:93,576,584-93,679,587 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0662, JHDM1E, CENP-35, KDM7C |
| Gene groups (HGNC) | PHD finger proteins; MicroRNA protein coding host genes; Lysine demethylase 7 family |
| Reactome | 3 pathways, smallest: HDMs demethylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O75151](https://www.uniprot.org/uniprotkb/O75151) (Lysine-specific demethylase PHF2):

> Lysine demethylase that demethylates both histones and non-histone proteins. Enzymatically inactive by itself, and becomes active following phosphorylation by PKA: forms a complex with ARID5B and mediates demethylation of methylated ARID5B. Demethylation of ARID5B leads to target the PHF2-ARID5B complex to target promoters, where PHF2 mediates demethylation of dimethylated 'Lys-9' of histone H3 (H3K9me2), followed by transcription activation of target genes. The PHF2-ARID5B complex acts as a …

**Summary**, from NCBI Gene [5253](https://www.ncbi.nlm.nih.gov/gene/5253):

> This gene encodes a protein which contains a zinc finger-like PHD (plant homeodomain) finger, distinct from other classes of zinc finger motifs, and a hydrophobic and highly conserved domain. The PHD finger shows the typical Cys4-His-Cys3 arrangement. PHD finger genes are thought to belong to a diverse group of transcriptional regulators possibly affecting eukaryotic gene expression by influencing chromatin structure. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8920) · Entrez [5253](https://www.ncbi.nlm.nih.gov/gene/5253) · UniProt [O75151](https://www.uniprot.org/uniprotkb/O75151) · Ensembl [ENSG00000197724](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197724)

## Data

Gene col 12448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12448); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12448]; `tensor/DDL_lfc|DDL_z.npy` [12448]; `embed/gene_vectors.npy` [12448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12448 or target_col == 12448). Every well: [[PHF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
