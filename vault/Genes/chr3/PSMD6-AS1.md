---
symbol: "PSMD6-AS1"
type: "gene"
col: 14356
ensembl_id: "ENSG00000243410"
name: "PSMD6 antisense RNA 1"
location: "3p14.1"
module: 83
arm: "+"
pooled_cpm: 5.66
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# PSMD6-AS1

*PSMD6 antisense RNA 1* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.01× (z +10.0, q 1e-20, up in 8 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +5.1, q 6e-05, up in 19 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.366× (z -9.5, q 9e-19, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R3F]] (+0.78, fdr 1e-05), [[PSMD6-AS2]] (+0.76, fdr 1e-05, ⚠ same locus), [[RFX3-DT]] (+0.74, fdr 3e-05), [[SPON1-AS1]] (+0.72, fdr 7e-06); moves opposite to [[MAST3]] (-0.71, fdr 1e-05), [[MALSU1]] (-0.71, fdr 1e-05), [[NDUFA12]] (-0.70, fdr 3e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[DDR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14356.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +10.0 | 1e-20 | 8/10 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +7.3 | 6e-11 | 22/29 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +7.0 | 6e-10 | 13/19 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.1 | 6e-05 | 19/39 (Panc 03.27, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.9 | 1e-04 | 15/40 (A-172, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +4.3 | 0.002 | 18/38 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.008 | 10/47 (NCI-H460, A498, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.43× | +3.2 | 0.11 | 7/43 (SK-MEL-2, A-427, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.41× | +3.1 | 0.12 | 7/43 (SW480, HS-578T, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14356.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.366×** | -9.5 | 9e-19 | 34/45 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.421×** | -8.2 | 7e-14 | 31/47 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.495×** | -6.7 | 5e-09 | 31/46 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.566×** | -5.1 | 4e-05 | 19/43 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.358×** | -5.1 | 4e-05 | 22/43 (RKO, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.655×** | -4.0 | 0.005 | 19/47 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.676×** | -3.7 | 0.015 | 20/41 (C-33 A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -3.7 | 0.018 | 13/43 (COLO 205, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -3.5 | 0.028 | 14/47 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fumaric acid (drug)]] 5 µM |  | **0.704×** | -3.2 | 0.072 | 6/46 (Panc 03.27, NCI-H2347, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14356. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.195× (z -9.2) |
| [[HT-29 (line)]] | alt | 6.72 | 0 | 2 (1 ⚠) | — | [[Vandetanib (drug)]] 0.5 µM 0.0822× (z -10.1) |
| [[LoVo (line)]] | wt | 7.06 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.120× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.126× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0931× (z -11.9) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.177× (z -8.7) |
| [[SW1417 (line)]] | alt | 4.53 | 0 | 2 | — | [[Sunitinib (drug)]] 0.05 µM 0.0782× (z -8.9) |
| [[A-427 (line)]] | wt | 5.35 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.104× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 6.94 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0729× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 6.61 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.115× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~49% of this change |
| [[NCI-H23 (line)]] | alt | 7.50 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0412× (z -12.6) |
| [[PANC-1 (line)]] | alt | 3.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.182× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 7.51 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.151× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14356), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R3F]] | +0.78 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[PSMD6-AS2]] | +0.76 | +0.83 / +0.53 | both halves | 1e-05 | same gene group; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RFX3-DT]] | +0.74 | +0.74 / +0.43 | both halves | 3e-05 |  |
| [[SPON1-AS1]] | +0.72 | +0.68 / +0.58 | both halves | 7e-06 | same gene group |
| [[ST7L]] | +0.72 | +0.72 / +0.36 | both halves | 1e-04 |  |
| [[SDCBP2-AS1]] | +0.72 | +0.66 / +0.59 | both halves | 7e-06 | same gene group |
| [[CCDC17]] | +0.72 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[SMIM15-AS1]] | +0.71 | +0.68 / +0.47 | both halves | 2e-05 | same gene group |
| [[LINC01191]] | +0.71 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.71 | +0.73 / +0.27 | both halves | 3e-04 | same gene group |
| [[GLIPR1-AS1]] | +0.71 | +0.65 / +0.47 | both halves | 2e-05 | same gene group |
| [[SLC2A9]] | +0.71 | +0.72 / +0.46 | both halves | 2e-05 |  |
| [[MCF2]] | +0.70 | +0.73 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.71 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[MALSU1]] | -0.71 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[NDUFA12]] | -0.70 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[ATG4C]] | -0.69 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MED23]] | -0.68 | -0.71 / -0.45 | both halves | 3e-05 |  |
| [[YIF1B]] | -0.68 | -0.55 / -0.43 | both halves | 4e-05 |  |
| [[FAM104A]] | -0.68 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[TUBG2]] | -0.67 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[SLC27A1]] | -0.67 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[DPY30]] | -0.66 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[BRAT1]] | -0.66 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[AP2S1]] | -0.66 | -0.54 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDR2]] | B | DDR2 activity raises PSMD6-AS1's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without DDR2 | 0.015 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[PRDM5]] | B | PRDM5 activity raises PSMD6-AS1's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.04× lower at baseline in the lines without PRDM5 | 0.074 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[RGS20]] | B | RGS20 activity raises PSMD6-AS1's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 1.11× lower at baseline in the lines without RGS20 | 0.080 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1 |
| [[HDAC6]] | B | HDAC6 activity raises PSMD6-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PSMD6-AS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity strengthens PSMD6-AS1's drug response | lines that do not express ITPR2-AS1 (4) vs lines expressing it (43) | the lines without ITPR2-AS1 respond 0.93× as strongly (z diff +0.29); strongest at Panobinostat 0.5 µM: 0.64x vs 0.35x (z diff +2.6) | 0.052 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17; target measured in part of the lines; both ways; artifact flags |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises PSMD6-AS1's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without ITPR2-AS1 | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (6.9, 7.3); signed map (18.9, 1.0). **Vector** length 73.9, 12.1% of its response variance represented; |z| ≥ 3 in 1,145 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +2.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.7 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -9.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -3.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | PSMD6 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p14.1 — chr3:64,011,964-64,016,246 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ENST00000462717, lnc00462717 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40480) · Entrez [109729140](https://www.ncbi.nlm.nih.gov/gene/109729140) · Ensembl [ENSG00000243410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243410)

## Data

Gene col 14356: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14356); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14356, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14356]; `tensor/DDL_lfc|DDL_z.npy` [14356]; `embed/gene_vectors.npy` [14356]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14356 or target_col == 14356). Every well: [[PSMD6-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD6-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
