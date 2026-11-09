---
symbol: "MIR9-3HG"
type: "gene"
col: 14947
ensembl_id: "ENSG00000255571"
name: "MIR9-3 host gene"
location: "15q26.1"
module: 19
arm: "+"
pooled_cpm: 4.84
n_lines_expressing: 29
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# MIR9-3HG

*MIR9-3 host gene* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +7.2, q 3e-10, up in 7 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.550× (z -6.5, q 5e-08, down in 17 of 26 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.440× (z -4.7, q 5e-04, down in 11 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.118×, NCI-H2030 0.177×, NCI-H1792 0.131×, C-33 A 0.178×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.135×, NCI-H2030 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0628×; ⚠ cell-cycle shift, explains ~59% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0827×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0683×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (C-33 A 0.0666×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEXMIF]] (+0.62, fdr 9e-06), [[EBF2]] (+0.56, fdr 1e-05), [[CNKSR2]] (+0.51, fdr 3e-05); moves opposite to [[TBCK]] (-0.42, fdr 1e-04), [[LINC02482]] (-0.40, fdr 4e-04), [[ITGA9-AS1]] (-0.40, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MPV17]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14947.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +7.2 | 3e-10 | 7/20 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +5.7 | 4e-06 | 13/26 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +5.2 | 3e-05 | 12/26 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.003 | 6/25 (SK-MEL-2, NCI-H1573, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.006 | 5/21 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ferulic acid (drug)]] 0.5 µM |  | 1.34× | +3.2 | 0.15 | 4/22 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.23× | +3.1 | 0.15 | 1/26 (C-33 A) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14947.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.118×, NCI-H2030 0.177×, NCI-H1792 0.131×, C-33 A 0.178×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.135×, NCI-H2030 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0628×; ⚠ cell-cycle shift, explains ~59% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0827×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0683×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (C-33 A 0.0666×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.550×** | -6.5 | 5e-08 | 17/26 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.577×** | -6.0 | 6e-07 | 14/23 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.571×** | -4.7 | 5e-04 | 14/18 (NCI-H1573, BT-474, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -4.7 | 5e-04 | 11/24 (NCI-H1792, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.679×** | -4.2 | 0.003 | 14/25 (NCI-H460, NCI-H1792, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.763×** | -4.2 | 0.003 | 10/22 (NCI-H23, NCI-H1573, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.683×** | -4.1 | 0.003 | 10/24 (SW1417, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.722×** | -3.5 | 0.029 | 8/24 (NCI-H1573, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.730×** | -3.4 | 0.039 | 7/26 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.692× | -3.1 | 0.12 | 6/24 (NCI-H2030, NCI-H1573, …) | rises with dose | composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 15.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0628× (z -15.2) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H1792 (line)]] | alt | 7.89 | 0 | 3 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0827× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 29.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 22.4 | 0 | 2 (1 ⚠) | — | [[XRK3F2 (drug)]] 0.5 µM 0.0666× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 8.67 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -9.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HOP62 (line)]] | alt | 4.11 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.101× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.766 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.337 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.801 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEXMIF]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 | **novel candidate** |
| [[EBF2]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CNKSR2]] | +0.51 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[ESYT3]] | +0.49 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[RADIL]] | +0.49 | +0.39 / +0.62 | both halves | 5e-05 |  |
| [[LGSN]] | +0.49 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[FAM124A]] | +0.49 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[SERPINB11]] | +0.47 | +0.52 / +0.35 | both halves | 1e-04 |  |
| [[RIMS1]] | +0.47 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[SLITRK5]] | +0.47 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[EYA2]] | +0.46 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[NCKAP5-AS2]] | +0.46 | +0.42 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCK]] | -0.42 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[LINC02482]] | -0.40 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[ITGA9-AS1]] | -0.40 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[MBD5]] | -0.38 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[MPV17]] | -0.38 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[TIMM9]] | -0.37 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[LINC00299]] | -0.37 | -0.37 / -0.25 | both halves | 4e-04 |  |
| [[TASP1]] | -0.36 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[NHLRC3]] | -0.36 | -0.32 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MIR9-3HG's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPV17]] | B | MIR9-3HG activity raises MPV17's level | lines that do not express MIR9-3HG (21) vs lines expressing it (29) | 1.21× lower at baseline in the lines without MIR9-3HG | 0.059 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, SNAP91 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.0, 39.4); signed map (40.9, 47.5). **Vector** length 37.4, 5.92% of its response variance represented; |z| ≥ 3 in 571 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.1 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.5 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +2.1 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.8 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.6 | -0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -1.5 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.4 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | -1.1 | -3.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | +0.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -1.7 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.7 | -0.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | MIR9-3 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q26.1 — chr15:89,361,579-89,424,983 (+) |
| Ensembl biotype | lncRNA |
| Also known as | BS-DRL1, lnc-FANCI-2; previously LINC00925 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27388) · Entrez [254559](https://www.ncbi.nlm.nih.gov/gene/254559) · Ensembl [ENSG00000255571](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255571)

## Data

Gene col 14947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14947); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14947]; `tensor/DDL_lfc|DDL_z.npy` [14947]; `embed/gene_vectors.npy` [14947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14947 or target_col == 14947). Every well: [[MIR9-3HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR9-3HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
