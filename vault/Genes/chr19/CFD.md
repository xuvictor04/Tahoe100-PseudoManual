---
symbol: "CFD"
type: "gene"
col: 12458
ensembl_id: "ENSG00000197766"
name: "complement factor D"
location: "19p13.3"
module: 85
arm: "+"
pooled_cpm: 12.59
n_lines_expressing: 45
n_dd_up: 7
n_dd_down: 31
n_dd_up_clean: 7
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 11
direction_downstream: 3
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# CFD

*complement factor D* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.53× (z +11.3, q 6e-27, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.221× (z -12.9, q 2e-35, down in 37 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARHSP1]] (+0.72, fdr 1e-05), [[RHPN2]] (+0.71, fdr 1e-05), [[PEDS1]] (+0.70, fdr 2e-05); moves opposite to [[PRDM5]] (-0.71, fdr 4e-05), [[AVEN]] (-0.69, fdr 1e-05), [[CSTF3]] (-0.66, fdr 2e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MLXIPL]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Peretinoin (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.53×** | +11.3 | 6e-27 | 41/43 (HT-29, C-33 A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.64×** | +8.4 | 2e-14 | 33/43 (Panc 03.27, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.61×** | +8.3 | 2e-14 | 36/41 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.48×** | +7.8 | 7e-13 | 34/43 (Panc 03.27, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.25×** | +7.0 | 3e-10 | 36/43 (C-33 A, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +6.2 | 5e-08 | 30/42 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.31×** | +3.8 | 0.013 | 16/41 (C-33 A, SNU-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.43× | +3.1 | 0.13 | 12/41 (PANC-1, A549, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.38× | +3.0 | 0.14 | 12/42 (AsPC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.221×** | -12.9 | 2e-35 | 37/41 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.348×** | -12.8 | 8e-35 | 35/41 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.292×** | -10.5 | 1e-23 | 37/43 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.340×** | -8.9 | 1e-16 | 37/42 (NCI-H1792, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.384×** | -8.2 | 4e-14 | 33/42 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.519×** | -7.9 | 2e-13 | 32/42 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.426×** | -7.3 | 3e-11 | 34/42 (NCI-H1792, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.424×** | -7.0 | 1e-10 | 25/37 (SW48, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.443×** | -6.9 | 2e-10 | 29/39 (Hs 766T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.515×** | -5.6 | 9e-07 | 27/42 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.518×** | -5.6 | 1e-06 | 23/41 (SNU-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.535×** | -5.0 | 2e-05 | 27/41 (SK-MEL-2, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.557×** | -5.0 | 3e-05 | 23/41 (LoVo, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.557×** | -5.0 | 3e-05 | 23/42 (PANC-1, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.365×** | -4.5 | 3e-04 | 23/42 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.592×** | -4.4 | 3e-04 | 23/42 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.369×** | -4.4 | 3e-04 | 25/39 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 34.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 23.4 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0832× (z -17.9) |
| [[SW48 (line)]] | wt | 28.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -13.4) |
| [[LoVo (line)]] | wt | 16.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 9.28 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.0208× (z -16.2) |
| [[A-172 (line)]] | wt | 22.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 30.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0673× (z -11.6) |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0356× (z -12.0) |
| [[A-427 (line)]] | wt | 23.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -11.6) |
| [[C-33 A (line)]] | alt | 12.1 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.56× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.109× (z -8.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 19.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -9.9) |
| [[LS 180 (line)]] | wt | 19.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -11.4) |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -8.5) |
| [[SW480 (line)]] | alt | 8.74 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -10.7) |
| [[A498 (line)]] | wt | 10.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.10× (z +8.8) | — |
| [[A549 (line)]] | wt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -10.6) |
| [[HT-29 (line)]] | alt | 6.25 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.14× (z +10.4) | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -10.4) ⚠ toxic |
| [[SW 900 (line)]] | alt | 7.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -10.9) |
| [[AN3 CA (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARHSP1]] | +0.72 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[RHPN2]] | +0.71 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.70 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SLC27A1]] | +0.70 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TNNI3]] | +0.68 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[MAST3]] | +0.67 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[LMTK3]] | +0.66 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[THRA]] | +0.66 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[FBXL16]] | +0.66 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ARRB2]] | +0.65 | +0.46 / +0.47 | both halves | 2e-05 | pathway: Platelet activation, signaling and aggregation |
| [[FAM13B]] | +0.65 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[VWA1]] | +0.65 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM5]] | -0.71 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[AVEN]] | -0.69 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[CSTF3]] | -0.66 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[LINC01829]] | -0.66 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[NIPAL2]] | -0.66 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PSME3IP1]] | -0.66 | -0.36 / -0.62 | both halves | 9e-05 |  |
| [[DESI1]] | -0.64 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[SPRY3]] | -0.63 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[MSANTD2]] | -0.63 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[PBLD]] | -0.63 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[N4BP2]] | -0.62 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[CRPPA]] | -0.62 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLXIPL]] | B | MLXIPL activity raises CFD's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 2.49× lower at baseline in the lines without MLXIPL | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[DUSP9]] | B | DUSP9 activity raises CFD's level | lines that do not express DUSP9 (17) vs lines expressing it (33) | 1.97× lower at baseline in the lines without DUSP9 | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC47A1, SMO, LAMC3 |
| [[PADI2]] | B | PADI2 activity raises CFD's level | lines that do not express PADI2 (21) vs lines expressing it (29) | 1.82× lower at baseline in the lines without PADI2 | 0.037 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, FBXO2 |
| [[TOP2A]] | B | TOP2A activity raises CFD's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CFD's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers CFD's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MCAM]] | B | MCAM activity lowers CFD's level | lines that do not express MCAM (21) vs lines expressing it (29) | 1.89× higher at baseline in the lines without MCAM | 0.062 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SMIM10, PPP2R2B, SLC16A6 |
| [[CKB]] | B | CKB activity raises CFD's level | lines that do not express CKB (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without CKB | 0.068 | ⚠ within organs, on part of the lines; also absent: BACH2, MAOA; maybe low, not absent |
| [[LINC00482]] | B | LINC00482 activity raises CFD's level | lines that do not express LINC00482 (8) vs lines expressing it (42) | 2.39× lower at baseline in the lines without LINC00482 | 0.083 | ⚠ within organs, on part of the lines; also absent: SOX13, SEPTIN9-DT |
| [[SMIM10]] | B | SMIM10 activity lowers CFD's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.71× higher at baseline in the lines without SMIM10 | 0.093 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[SYP]] | C | SYP activity raises CFD's level | lines that do not express SYP (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without SYP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Peretinoin (drug)]] 0.5 µM | C | CFD activity raises the cells' numbers under Peretinoin 0.5 µM (protects the cells) | lines that do not express CFD (5) vs lines expressing it (43) | the lines without CFD: 0.63× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs; also absent: KIAA1671, ENSG00000291079, ATP11A |
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | C | CFD activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express CFD (5) vs lines expressing it (43) | the lines without CFD: 0.76× the cells of the other lines | 0.057 | ⚠ tissue-confounded; across organs; also absent: KIAA1671, ENSG00000291079, ATP11A |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | C | CFD activity raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | lines that do not express CFD (5) vs lines expressing it (43) | the lines without CFD: 0.82× the cells of the other lines | 0.098 | ⚠ tissue-confounded; across organs; also absent: KIAA1671, ENSG00000291079, ATP11A |

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (7.5, -3.0); signed map (-28.3, 19.9). **Vector** length 97.1, 25.3% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +11.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.0 | +8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.0 | +7.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.2 | +6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -12.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.8 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | complement factor D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:859,453-867,884 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ADN; previously DF, PFD |
| Gene groups (HGNC) | Granule associated serine proteases of immune defence; Complement system activation components |
| Hallmark sets | COAGULATION, MYOGENESIS |
| Reactome | 9 pathways, smallest: Alternative complement activation; Initial triggering of complement; Complement cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P00746](https://www.uniprot.org/uniprotkb/P00746) (Complement factor D):

> Serine protease that initiates the alternative pathway of the complement system, a cascade of proteins that leads to phagocytosis and breakdown of pathogens and signaling that strengthens the adaptive immune system. In contrast to other complement pathways (classical, lectin and GZMK) that are directly activated by pathogens or antigen-antibody complexes, the alternative complement pathway is initiated by the spontaneous hydrolysis of complement C3. The alternative complement pathway acts as an …

**Summary**, from NCBI Gene [1675](https://www.ncbi.nlm.nih.gov/gene/1675):

> This gene encodes a member of the S1, or chymotrypsin, family of serine peptidases. This protease catalyzes the cleavage of factor B, the rate-limiting step of the alternative pathway of complement activation. This protein also functions as an adipokine, a cell signaling protein secreted by adipocytes, which regulates insulin secretion in mice. Mutations in this gene underlie complement factor D deficiency, which is associated with recurrent bacterial meningitis infections in human patients. …

**Accessions** — [HGNC:2771](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2771) · Entrez [1675](https://www.ncbi.nlm.nih.gov/gene/1675) · UniProt [P00746](https://www.uniprot.org/uniprotkb/P00746) · Ensembl [ENSG00000197766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197766)

## Data

Gene col 12458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12458); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12458]; `tensor/DDL_lfc|DDL_z.npy` [12458]; `embed/gene_vectors.npy` [12458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12458 or target_col == 12458). Every well: [[CFD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
