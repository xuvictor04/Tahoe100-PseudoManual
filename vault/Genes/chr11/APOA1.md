---
symbol: "APOA1"
type: "gene"
col: 3964
ensembl_id: "ENSG00000118137"
name: "apolipoprotein A1"
location: "11q23.3"
module: 8
arm: "+"
pooled_cpm: 3.58
n_lines_expressing: 7
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# APOA1

*apolipoprotein A1* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 10.7× (z +9.3, q 7e-18, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.86× (z +7.5, q 1e-11, up in 2 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.227×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHSG]] (+0.71, fdr 7e-06), [[ALB]] (+0.63, fdr 7e-06), [[AMBP]] (+0.59, fdr 1e-05); moves opposite to [[MTAP]] (-0.52, fdr 3e-04), [[IFRD2]] (-0.49, fdr 1e-04), [[PGAM5]] (-0.49, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SERPINF1]] → it (grade C ⚠); 5 go from it, the strongest it → [[SLC7A8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **10.7×** | +9.3 | 7e-18 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.20×** | +8.0 | 5e-13 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.86×** | +7.5 | 1e-11 | 2/2 (HepG2/C3A, KATO III) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.12×** | +5.9 | 4e-07 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.74×** | +5.0 | 6e-05 | 1/1 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.55×** | +5.0 | 6e-05 | 1/1 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.11×** | +4.1 | 0.003 | 1/2 (HepG2/C3A) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **2.02×** | +3.9 | 0.007 | 0/2 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **6.51×** | +3.9 | 0.007 | 1/1 (HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +3.3 | 0.052 | 1/2 (HepG2/C3A) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **2.31×** | +3.3 | 0.052 | 0/1 | inconsistent across doses | low cells (technical?) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.21×** | +3.1 | 0.090 | 0/2 | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.227×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 273 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.346 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.797 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.893 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.663 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.393 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 14 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSG]] | +0.71 | +0.77 / +0.86 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 944 |
| [[ALB]] | +0.63 | +0.67 / +0.78 | both halves | 7e-06 | pathway: Binding and Uptake of Ligands by Scavenger Receptors; STRING 998 |
| [[AMBP]] | +0.59 | +0.68 / +0.56 | both halves | 1e-05 | pathway: Binding and Uptake of Ligands by Scavenger Receptors; STRING 891 |
| [[CRIP1]] | +0.55 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[SERF2]] | +0.53 | +0.27 / +0.45 | both halves | 3e-04 |  |
| [[HLA-DRB1]] | +0.52 | +0.20 / +0.45 | both halves | 7e-04 |  |
| [[AFP]] | +0.51 | +0.83 / +0.69 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 721 |
| [[IGFBP2]] | +0.50 | +0.35 / +0.32 | both halves | 2e-04 | pathway: Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| [[APOH]] | +0.50 | +0.59 / +0.68 | both halves | 7e-06 | same gene group; pathway: Platelet activation, signaling and aggregation; STRING 985 |
| [[SELENOP]] | +0.50 | +0.40 / +0.42 | both halves | 5e-05 | pathway: Platelet activation, signaling and aggregation; STRING 580 |
| [[GCHFR]] | +0.50 | +0.43 / +0.26 | both halves | 3e-04 | pathway: Metabolism of vitamins and cofactors |
| [[AGT]] | +0.49 | +0.54 / +0.51 | both halves | 1e-05 | pathway: PPARA activates gene expression; STRING 553 |

## Genes that move opposite

*39 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTAP]] | -0.52 | -0.27 / -0.36 | both halves | 3e-04 |  |
| [[IFRD2]] | -0.49 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[PGAM5]] | -0.49 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[PSMG1]] | -0.48 | -0.28 / -0.34 | both halves | 3e-04 |  |
| [[IDE]] | -0.47 | -0.30 / -0.32 | both halves | 2e-04 |  |
| [[PRMT5]] | -0.47 | -0.34 / -0.29 | both halves | 2e-04 |  |
| [[DPM2]] | -0.46 | -0.33 / -0.36 | both halves | 1e-04 | pathway: Dengue Virus Genome Translation and Replication |
| [[WDR77]] | -0.45 | -0.17 / -0.36 | ⚠ not reproduced | 0.001 |  |
| [[PSMD11]] | -0.44 | -0.30 / -0.32 | both halves | 2e-04 | pathway: ABC transporter disorders |
| [[SH3D19]] | -0.44 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[EIF6]] | -0.44 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[PSMC5]] | -0.44 | -0.31 / -0.24 | both halves | 5e-04 | pathway: ABC transporter disorders |
| [[DESI1]] | -0.43 | -0.26 / -0.32 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINF1]] | C | SERPINF1 activity raises APOA1's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.62× lower at baseline in the lines without SERPINF1 | 0.012 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent; co-absent with the target |
| [[HLA-DRA]] | C | HLA-DRA activity raises APOA1's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.23× lower at baseline in the lines without HLA-DRA | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530; co-absent with the target |
| [[PIGR]] | C | PIGR activity raises APOA1's level | lines that do not express PIGR (45) vs lines expressing it (5) | 1.54× lower at baseline in the lines without PIGR | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises APOA1's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 1.15× lower at baseline in the lines without WFDC2 | 0.074 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[HLA-DRB1]] | C | HLA-DRB1 activity raises APOA1's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.12× lower at baseline in the lines without HLA-DRB1 | 0.084 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC7A8]] | B | APOA1 activity raises SLC7A8's level | lines that do not express APOA1 (43) vs lines expressing it (7) | 1.29× lower at baseline in the lines without APOA1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: AFP, APOA2, APOB |
| [[HLA-DRA]] | C | APOA1 activity raises HLA-DRA's level | lines that do not express APOA1 (43) vs lines expressing it (7) | 1.68× lower at baseline in the lines without APOA1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: AFP, APOA2, APOB; co-absent with the target |
| [[AZGP1]] | C | APOA1 activity raises AZGP1's level | lines that do not express APOA1 (43) vs lines expressing it (7) | 2.72× lower at baseline in the lines without APOA1 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: AFP, APOA2, APOB; co-absent with the target |
| [[LYZ]] | C | APOA1 activity raises LYZ's level | lines that do not express APOA1 (43) vs lines expressing it (7) | 3.94× lower at baseline in the lines without APOA1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: AFP, APOA2, APOB; co-absent with the target |
| [[PLA2G2A]] | C | APOA1 activity raises PLA2G2A's level | lines that do not express APOA1 (43) vs lines expressing it (7) | 3.30× lower at baseline in the lines without APOA1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: AFP, APOA2, APOB; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.188). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.2, 55.1); signed map (66.8, 20.0). **Vector** length 6.04, 2.01% of its response variance represented; |z| ≥ 3 in 37 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +0.5 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.4 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.4 | +7.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.3 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.2 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.2 | +0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.2 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.2 | +0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.3 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.2 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.2 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.2 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.2 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.2 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.1 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.1 | +1.7 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:116,835,751-116,837,622 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Apolipoproteins |
| Hallmark sets | BILE_ACID_METABOLISM, COAGULATION |
| Reactome | 43 pathways, smallest: Chylomicron remodeling; HDL clearance; Chylomicron assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P02647](https://www.uniprot.org/uniprotkb/P02647) (Apolipoprotein A-I):

> Participates in the reverse transport of cholesterol from tissues to the liver for excretion by promoting cholesterol efflux from tissues and by acting as a cofactor for the lecithin cholesterol acyltransferase (LCAT). As part of the SPAP complex, activates spermatozoa motility.

**Summary**, from NCBI Gene [335](https://www.ncbi.nlm.nih.gov/gene/335):

> This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plasma cholesteryl esters. This gene is closely linked with two other apolipoprotein genes on …

**Accessions** — [HGNC:600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:600) · Entrez [335](https://www.ncbi.nlm.nih.gov/gene/335) · UniProt [P02647](https://www.uniprot.org/uniprotkb/P02647) · Ensembl [ENSG00000118137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118137)

## Data

Gene col 3964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3964); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3964]; `tensor/DDL_lfc|DDL_z.npy` [3964]; `embed/gene_vectors.npy` [3964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3964 or target_col == 3964). Every well: [[APOA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
