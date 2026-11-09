---
symbol: "FRMPD3"
type: "gene"
col: 7165
ensembl_id: "ENSG00000147234"
name: "FERM and PDZ domain containing 3"
location: "Xq22.3"
module: 115
arm: "+"
pooled_cpm: 2.81
n_lines_expressing: 32
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# FRMPD3

*FERM and PDZ domain containing 3* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.86× (z +17.5, q 0e+00, up in 11 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.632× (z -4.2, q 0.013, down in 14 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRP4]] (+0.64, fdr 8e-06), [[TSPAN12]] (+0.61, fdr 3e-05), [[PROM2]] (+0.58, fdr 3e-05); moves opposite to [[TRAPPC12]] (-0.57, fdr 2e-05), [[TATDN1]] (-0.46, fdr 9e-05), [[TTC17]] (-0.45, fdr 1e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[PIGL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7165.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.86×** | +17.5 | 0e+00 | 11/21 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.76×** | +13.1 | 9e-37 | 20/26 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.35×** | +10.6 | 5e-24 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.89×** | +9.7 | 5e-20 | 1/9 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +8.5 | 2e-15 | 1/5 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.39×** | +7.9 | 2e-13 | 16/22 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.04×** | +6.5 | 7e-09 | 18/27 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.8 | 1e-04 | 6/26 (SW480, A549, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.97×** | +4.4 | 6e-04 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.65×** | +4.4 | 7e-04 | 2/19 (NCI-H460, LoVo) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.62×** | +4.2 | 0.001 | 2/12 (HCT15, J82) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.38×** | +4.1 | 0.002 | 0/8 | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.50×** | +3.7 | 0.011 | 6/26 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.4 | 0.028 | 2/14 (PANC-1, SW 900) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.47×** | +3.3 | 0.032 | 4/20 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +3.3 | 0.040 | 6/23 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.064 | 1/17 (NCI-H1573) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +2.9 | 0.097 | 3/18 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.38×** | +2.9 | 0.097 | 4/26 (BT-474, NCI-H2347, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7165.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.632×** | -4.2 | 0.013 | 14/27 (COLO 205, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.747×** | -3.8 | 0.038 | 12/25 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.677×** | -3.6 | 0.060 | 3/27 (NCI-H1573, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 55.3 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -20.5) |
| [[AN3 CA (line)]] | alt | 34.9 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0665× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 0.964 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +8.8) | — |
| [[A-172 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.773 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.745 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.856 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.593 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.937 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.917 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP4]] | +0.64 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[TSPAN12]] | +0.61 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[PROM2]] | +0.58 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[CDH24]] | +0.57 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[LINC00937]] | +0.57 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[AMOT]] | +0.56 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[TLE2]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ATP8B1]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SUSD4]] | +0.54 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[ARSL]] | +0.54 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[NDRG2]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[PITX2]] | +0.53 | +0.41 / +0.64 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC12]] | -0.57 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[TATDN1]] | -0.46 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[TTC17]] | -0.45 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[MSS51]] | -0.44 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[LMF1]] | -0.44 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[DNAJC16]] | -0.44 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[PIGL]] | -0.43 | -0.29 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FRMPD3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BARX2]] | B | BARX2 activity raises FRMPD3's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 1.76× lower at baseline in the lines without BARX2 | 0.043 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[RHOV]] | B | RHOV activity raises FRMPD3's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without RHOV | 0.061 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[MGC32805]] | B | MGC32805 activity raises FRMPD3's level | lines that do not express MGC32805 (32) vs lines expressing it (18) | 2.28× lower at baseline in the lines without MGC32805 | 0.074 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent |
| [[GRHL3]] | B | GRHL3 activity raises FRMPD3's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 1.84× lower at baseline in the lines without GRHL3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIGL]] | B | FRMPD3 activity lowers PIGL's level | lines that do not express FRMPD3 (18) vs lines expressing it (32) | 1.42× higher at baseline in the lines without FRMPD3 | 0.009 | ⚠ within organs, on part of the lines; also absent: CACNG4, NSUN7, GYG2; maybe low, not absent |
| [[ARHGAP44]] | B | FRMPD3 activity lowers ARHGAP44's level | lines that do not express FRMPD3 (18) vs lines expressing it (32) | 1.79× higher at baseline in the lines without FRMPD3 | 0.028 | ⚠ within organs, on part of the lines; also absent: CACNG4, NSUN7, GYG2; maybe low, not absent |
| [[DAPK2]] | B | FRMPD3 activity raises DAPK2's level | lines that do not express FRMPD3 (18) vs lines expressing it (32) | 1.76× lower at baseline in the lines without FRMPD3 | 0.044 | ⚠ within organs, on part of the lines; also absent: CACNG4, NSUN7, GYG2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.1, 48.5); signed map (52.3, 0.9). **Vector** length 45.7, 8.25% of its response variance represented; |z| ≥ 3 in 648 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +13.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +17.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.0 | +2.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -1.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | FERM and PDZ domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:107,449,652-107,605,255 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP5-1070B1.1, KIAA1817 |
| Gene groups (HGNC) | PDZ domain containing; FERM domain containing |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

UniProt [Q5JV73](https://www.uniprot.org/uniprotkb/Q5JV73) carries no function annotation.

**Summary**, from NCBI Gene [84443](https://www.ncbi.nlm.nih.gov/gene/84443):

> This gene encodes a protein that contains a PDZ (post synaptic density protein (PSD95), Drosophila disc large tumor suppressor (Dlg1), and zonula occludens-1 protein (zo-1) domain at the N-terminus followed by a FERM domain. The encoded protein is involved in signal transduction. The PDZ domain is thought to function in protein-protein interactions, mainly by binding to specific C-terminal peptides of other proteins. The FERM domain is found in proteins that are localized to the plasma membrane …

**Accessions** — [HGNC:29382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29382) · Entrez [84443](https://www.ncbi.nlm.nih.gov/gene/84443) · UniProt [Q5JV73](https://www.uniprot.org/uniprotkb/Q5JV73) · Ensembl [ENSG00000147234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147234)

## Data

Gene col 7165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7165); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7165]; `tensor/DDL_lfc|DDL_z.npy` [7165]; `embed/gene_vectors.npy` [7165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7165 or target_col == 7165). Every well: [[FRMPD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRMPD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
