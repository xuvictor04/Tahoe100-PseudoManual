---
symbol: "KCNIP3"
type: "gene"
col: 3615
ensembl_id: "ENSG00000115041"
name: "potassium voltage-gated channel interacting protein 3"
location: "2q11.1"
module: 102
arm: "+"
pooled_cpm: 3.32
n_lines_expressing: 44
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# KCNIP3

*potassium voltage-gated channel interacting protein 3* — 2q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.52× (z +13.1, q 1e-36, up in 21 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.500× (z -9.9, q 3e-20, down in 23 of 29 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.606× (z -5.1, q 8e-05, down in 14 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 0.165×, NCI-H23 0.178×, BT-474 0.151×, NCI-H2030 0.135×; ⚠ cell-cycle shift, explains ~53% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (BT-474 0.0744×; ⚠ transcription drop); [[Pemetrexed (drug)]] 5 µM in 1 line (NCI-H23 0.0938×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SNU-423 0.0475×).
> Its strongest partners by |cos| (78 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSI1]] (+0.55, fdr 4e-05), [[RBPMS2]] (+0.54, fdr 4e-05), [[MRAS]] (+0.53, fdr 1e-04); moves opposite to [[INIP]] (-0.58, fdr 4e-05), [[SNAP29]] (-0.53, fdr 2e-04), [[GPATCH11]] (-0.50, fdr 3e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00466]] → it (grade B ⚠); 2 go from it, the strongest it → [[GOLM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +13.1 | 1e-36 | 21/32 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.32×** | +7.8 | 1e-12 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +7.8 | 1e-12 | 1/5 (A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +6.0 | 2e-07 | 2/16 (SNU-423, HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +5.2 | 2e-05 | 18/39 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +5.0 | 5e-05 | 8/35 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.4 | 8e-04 | 13/36 (HEC-1-A, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.3 | 0.001 | 10/28 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.024 | 5/39 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.029 | 6/40 (A-172, NCI-H460, …) | rises with dose | position effect removed |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.43×** | +3.3 | 0.045 | 4/27 (A549, HT-29, …) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.3 | 0.052 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.2 | 0.062 | 2/20 (SW480, NCI-H23) | rises with dose | cell-cycle shift (explains ~18% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3615.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 0.165×, NCI-H23 0.178×, BT-474 0.151×, NCI-H2030 0.135×; ⚠ cell-cycle shift, explains ~53% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (BT-474 0.0744×; ⚠ transcription drop); [[Pemetrexed (drug)]] 5 µM in 1 line (NCI-H23 0.0938×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SNU-423 0.0475×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.500×** | -9.9 | 3e-20 | 23/29 (PANC-1, NCI-H23, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.487×** | -7.0 | 8e-10 | 19/36 (NCI-H23, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.606×** | -5.1 | 8e-05 | 14/39 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.629×** | -4.7 | 4e-04 | 14/38 (SNU-423, SHP-77, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.631×** | -4.7 | 4e-04 | 12/36 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.648×** | -4.4 | 0.001 | 16/38 (A-172, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.654×** | -4.3 | 0.001 | 17/29 (NCI-H460, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.667×** | -4.1 | 0.003 | 12/36 (NCI-H23, SHP-77, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.472×** | -4.0 | 0.005 | 9/33 (COLO 205, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.680×** | -3.9 | 0.005 | 13/40 (BT-474, NCI-H23, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 6.45 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.55× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -10.1) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Pemetrexed (drug)]] 5 µM 0.0938× (z -9.4) |
| [[BT-474 (line)]] | alt | 8.62 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -9.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H460 (line)]] | wt | 6.13 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.49× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -9.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 2.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +8.5) | — |
| [[LoVo (line)]] | wt | 2.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 4.68 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -9.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[PANC-1 (line)]] | alt | 4.97 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -13.8) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SNU-423 (line)]] | alt | 3.19 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0475× (z -8.8) |
| [[A-172 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.942 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.911 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 21 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSI1]] | +0.55 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[RBPMS2]] | +0.54 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[MRAS]] | +0.53 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[NCS1]] | +0.52 | +0.50 / +0.49 | both halves | 1e-05 | same gene group |
| [[UBXN8]] | +0.51 | +0.23 / +0.52 | both halves | 5e-04 |  |
| [[ENTPD1]] | +0.50 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[SCAMP5]] | +0.50 | +0.28 / +0.39 | both halves | 3e-04 |  |
| [[LINC02026]] | +0.49 | +0.31 / +0.44 | both halves | 2e-04 |  |
| [[INPPL1]] | +0.49 | +0.36 / +0.26 | both halves | 4e-04 |  |
| [[MYLK4]] | +0.49 | +0.13 / +0.38 | ⚠ not reproduced | 0.002 |  |
| [[SLC7A7]] | +0.49 | +0.19 / +0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[LURAP1]] | +0.48 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[MATN3]] | +0.48 | +0.29 / +0.50 | both halves | 2e-04 |  |
| [[ATXN7L3-AS1]] | +0.48 | +0.30 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INIP]] | -0.58 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[SNAP29]] | -0.53 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[GPATCH11]] | -0.50 | -0.40 / -0.27 | both halves | 3e-04 |  |
| [[POLM]] | -0.49 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[SENP2]] | -0.49 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[TTC26]] | -0.48 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[WDR70]] | -0.48 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[DOP1A]] | -0.46 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[CAAP1]] | -0.46 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[ZBTB48]] | -0.46 | -0.38 / -0.26 | both halves | 4e-04 |  |
| [[FRA10AC1]] | -0.46 | -0.37 / -0.22 | both halves | 6e-04 |  |
| [[DNTTIP1]] | -0.46 | -0.40 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00466]] | B | LINC00466 activity raises KCNIP3's level | lines that do not express LINC00466 (15) vs lines expressing it (35) | 1.64× lower at baseline in the lines without LINC00466 | 0.086 | ⚠ within organs, on part of the lines; also absent: FAM124A, NTN1, SSPOP; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises KCNIP3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GOLM1]] | B | KCNIP3 activity raises GOLM1's level | lines that do not express KCNIP3 (6) vs lines expressing it (44) | 1.80× lower at baseline in the lines without KCNIP3 | 0.068 | ⚠ within organs, on part of the lines; also absent: MCF2L2, GOLGA2P5-1, DMBX1 |
| [[SENP2]] | B | KCNIP3 activity raises SENP2's level | lines that do not express KCNIP3 (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without KCNIP3 | 0.086 | ⚠ within organs, on part of the lines; also absent: MCF2L2, GOLGA2P5-1, DMBX1 |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.6, 35.3); signed map (38.4, -1.1). **Vector** length 52.2, 7.15% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.8 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.7 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -1.6 | -7.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.3 | -4.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -0.8 |
|  | [[Malotilate (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.0 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel interacting protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.1 — chr2:95,297,327-95,386,077 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DREAM, KCHIP3; previously CSEN |
| Gene groups (HGNC) | Potassium voltage-gated channel regulatory subunits; EF-hand domain containing |
| Hallmark sets | COMPLEMENT |
| Reactome | 6 pathways, smallest: Regulation of NPAS4 gene transcription; Phase 1 - inactivation of fast Na+ channels; Regulation of NPAS4 gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2W7](https://www.uniprot.org/uniprotkb/Q9Y2W7) (Calsenilin):

> Calcium-dependent transcriptional repressor that binds to the DRE element of genes including PDYN and FOS. Affinity for DNA is reduced upon binding to calcium and enhanced by binding to magnesium. Seems to be involved in nociception (By similarity).; Regulatory subunit of Kv4/D (Shal)-type voltage-gated rapidly inactivating A-type potassium channels, such as KCND2/Kv4.2 and KCND3/Kv4.3. Modulates channel expression at the cell membrane, gating characteristics, inactivation kinetics and rate of …

**Summary**, from NCBI Gene [30818](https://www.ncbi.nlm.nih.gov/gene/30818):

> This gene encodes a member of the family of voltage-gated potassium (Kv) channel-interacting proteins, which belong to the recoverin branch of the EF-hand superfamily. Members of this family are small calcium binding proteins containing EF-hand-like domains. They are integral subunit components of native Kv4 channel complexes that may regulate A-type currents, and hence neuronal excitability, in response to changes in intracellular calcium. The encoded protein also functions as a …

**Accessions** — [HGNC:15523](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15523) · Entrez [30818](https://www.ncbi.nlm.nih.gov/gene/30818) · UniProt [Q9Y2W7](https://www.uniprot.org/uniprotkb/Q9Y2W7) · Ensembl [ENSG00000115041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115041)

## Data

Gene col 3615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3615); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3615]; `tensor/DDL_lfc|DDL_z.npy` [3615]; `embed/gene_vectors.npy` [3615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3615 or target_col == 3615). Every well: [[KCNIP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNIP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
