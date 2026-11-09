---
symbol: "B3GNT9"
type: "gene"
col: 14118
ensembl_id: "ENSG00000237172"
name: "UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 9"
location: "16q22.1"
module: 13
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# B3GNT9

*UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 9* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.55× (z +7.8, q 5e-12, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vilanterol (drug)]] 0.5 µM: 1.50× (z +3.5, q 0.070, up in 3 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.408× (z -7.7, q 9e-12, down in 20 of 38 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MXRA5]] (+0.63, fdr 1e-05), [[ARHGEF6]] (+0.62, fdr 1e-05), [[CHST14]] (+0.58, fdr 4e-05); moves opposite to [[KIAA1958]] (-0.51, fdr 1e-04), [[FBXL4]] (-0.50, fdr 3e-05), [[UQCRH]] (-0.50, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[SIRLNT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14118.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +7.8 | 5e-12 | 1/2 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +5.4 | 1e-05 | 2/4 (A-172, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +5.3 | 2e-05 | 7/12 (Hs 766T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.070 | 3/27 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.45× | +3.2 | 0.14 | 5/35 (Hs 766T, A549, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.18 | 1/36 (SW480) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.28× | +3.0 | 0.18 | 2/41 (HOP62, J82) | top dose only | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.42× | +3.0 | 0.18 | 6/35 (HEC-1-A, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14118.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.408×** | -7.7 | 9e-12 | 20/38 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.427×** | -7.3 | 9e-11 | 23/43 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.499×** | -6.0 | 5e-07 | 19/42 (A-172, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.504×** | -5.9 | 6e-07 | 21/37 (A-172, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.599×** | -4.4 | 0.001 | 15/38 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.629×** | -4.0 | 0.007 | 12/32 (SW480, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.648×** | -3.7 | 0.017 | 10/41 (MIA PaCa-2, H4, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.655×** | -3.6 | 0.022 | 8/41 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.670×** | -3.4 | 0.040 | 10/42 (hTERT-HPNE, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -3.0 | 0.14 | 9/46 (SW48, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.22 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0254× (z -16.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.136× (z -9.1) |
| [[J82 (line)]] | alt | 6.05 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0808× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 2.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.112× (z -8.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 0.754 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.609 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.856 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.812 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.717 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.716 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.780 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.935 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.785 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.561 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.642 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.898 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.720 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXRA5]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ARHGEF6]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CHST14]] | +0.58 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[TEK]] | +0.55 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[RUSC1-AS1]] | +0.55 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ZNF747]] | +0.55 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[LRRC17]] | +0.54 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[ZBTB45]] | +0.54 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[IPO9-AS1]] | +0.53 | +0.53 / +0.36 | both halves | 9e-05 |  |
| [[HHIPL2]] | +0.53 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[MAGED2]] | +0.52 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[PDGFRB]] | +0.52 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1958]] | -0.51 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[FBXL4]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[UQCRH]] | -0.50 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[TPD52]] | -0.49 | -0.51 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[NAA10]] ⚠ | -0.48 | -0.38 / -0.29 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CLMN]] | -0.48 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[FAM117B]] | -0.48 | -0.49 / -0.26 | both halves | 3e-04 |  |
| [[RALGAPA2]] | -0.48 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[SH3GL3]] | -0.48 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[RPL13]] | -0.47 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[SNX25]] | -0.47 | -0.43 / -0.24 | both halves | 4e-04 |  |
| [[EIF3K]] | -0.47 | -0.34 / -0.26 | both halves | 4e-04 |  |
| [[FAM118A]] | -0.46 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[RPL27]] | -0.45 | -0.36 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIRLNT]] | B | SIRLNT activity raises B3GNT9's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 1.72× lower at baseline in the lines without SIRLNT | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[ARHGEF6]] | B | ARHGEF6 activity raises B3GNT9's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 1.54× lower at baseline in the lines without ARHGEF6 | 0.016 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[PDGFRB]] | B | PDGFRB activity raises B3GNT9's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 1.85× lower at baseline in the lines without PDGFRB | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[COL1A1]] | B | COL1A1 activity raises B3GNT9's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 1.53× lower at baseline in the lines without COL1A1 | 0.035 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411 |
| [[COL5A1]] | B | COL5A1 activity raises B3GNT9's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 1.70× lower at baseline in the lines without COL5A1 | 0.045 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[FBN1]] | B | FBN1 activity raises B3GNT9's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without FBN1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[HDAC6]] | B | HDAC6 activity raises B3GNT9's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PDGFRB]] | B | PDGFRB activity strengthens B3GNT9's drug response | lines that do not express PDGFRB (34) vs lines expressing it (10) | the lines without PDGFRB respond 0.38× as strongly (z diff +1.97); strongest at Belinostat 5 µM: 0.48x vs 0.24x (z diff +2.9) | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; target measured in part of the lines; artifact flags |
| [[HTRA3]] | B | HTRA3 activity raises B3GNT9's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 1.59× lower at baseline in the lines without HTRA3 | 0.074 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[SSPN]] | B | SSPN activity raises B3GNT9's level | lines that do not express SSPN (15) vs lines expressing it (35) | 1.50× lower at baseline in the lines without SSPN | 0.099 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.420). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (56.4, 20.4); signed map (42.2, 30.6). **Vector** length 39.1, 4.32% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +2.3 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | -0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +2.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.0 | +2.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.7 | -7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -1.4 | -2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.3 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.2 | -7.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,148,104-67,150,998 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4655 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

UniProt [Q6UX72](https://www.uniprot.org/uniprotkb/Q6UX72) carries no function annotation.

**Summary**, from NCBI Gene [84752](https://www.ncbi.nlm.nih.gov/gene/84752):

> Predicted to enable UDP-glycosyltransferase activity. Predicted to be involved in poly-N-acetyllactosamine biosynthetic process. Predicted to be located in membrane. Predicted to be active in Golgi membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28714) · Entrez [84752](https://www.ncbi.nlm.nih.gov/gene/84752) · UniProt [Q6UX72](https://www.uniprot.org/uniprotkb/Q6UX72) · Ensembl [ENSG00000237172](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237172)

## Data

Gene col 14118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14118); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14118]; `tensor/DDL_lfc|DDL_z.npy` [14118]; `embed/gene_vectors.npy` [14118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14118 or target_col == 14118). Every well: [[B3GNT9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GNT9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
