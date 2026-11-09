---
symbol: "TLR4"
type: "gene"
col: 5925
ensembl_id: "ENSG00000136869"
name: "toll like receptor 4"
location: "9q33.1"
module: 151
arm: "+"
pooled_cpm: 2.58
n_lines_expressing: 24
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# TLR4

*toll like receptor 4* — 9q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.09× (z +10.5, q 7e-23, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.67× (z +4.8, q 1e-04, up in 6 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.540× (z -4.2, q 0.009, down in 10 of 19 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLPP4]] (+0.64, fdr 1e-05), [[LINC02930]] (+0.62, fdr 1e-05), [[SRPX2]] (+0.55, fdr 1e-05); moves opposite to [[CBFA2T2]] (-0.52, fdr 5e-05), [[KDM4B]] (-0.51, fdr 3e-05), [[CCNI]] (-0.49, fdr 3e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 9 go from it, the strongest it → [[CBFA2T2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5925.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.09×** | +10.5 | 7e-23 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.62×** | +9.5 | 9e-19 | 1/6 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +7.4 | 3e-11 | 2/9 (J82, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.8 | 1e-04 | 2/11 (HOP62, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.67×** | +4.8 | 1e-04 | 6/19 (SW480, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.73×** | +4.8 | 1e-04 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.05×** | +4.8 | 1e-04 | 4/15 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +4.8 | 1e-04 | 5/21 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +4.6 | 2e-04 | 7/18 (J82, CHP-212, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.84×** | +4.0 | 0.003 | 1/12 (SW480) | inconsistent across doses | low cells (technical?) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.81×** | +3.7 | 0.013 | 0/12 | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.73×** | +3.6 | 0.013 | 0/13 | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.5 | 0.018 | 0/13 | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.3 | 0.041 | 1/12 (RPMI-7951) | top dose only | cell-cycle shift (explains ~6% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.54×** | +3.3 | 0.043 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.62×** | +3.2 | 0.046 | 6/19 (RPMI-7951, A-172, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.64×** | +3.1 | 0.062 | 6/18 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.068 | 4/21 (J82, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.540×** | -4.2 | 0.009 | 10/19 (SK-MEL-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.540×** | -4.2 | 0.009 | 11/19 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.548×** | -3.8 | 0.033 | 5/19 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.597×** | -3.5 | 0.068 | 12/19 (Hs 766T, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.19 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0497× (z -9.0) |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -9.4) |
| [[SW480 (line)]] | alt | 2.13 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0666× (z -8.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 0.143 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.634 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.219 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.194 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.738 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.182 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.162 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.154 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.192 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.809 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.194 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.201 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.224 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.226 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLPP4]] | +0.64 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[LINC02930]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SRPX2]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[MILR1]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SUSD5]] | +0.52 | +0.42 / +0.33 | both halves | 1e-04 |  |
| [[IL7R]] | +0.51 | +0.49 / +0.39 | both halves | 5e-05 | same gene group; STRING 490 |
| [[ZNF300]] | +0.50 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[SPOCK3]] | +0.50 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[MAML2]] | +0.50 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[SLFN12]] | +0.49 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[KCTD12]] | +0.48 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[NOL11]] | +0.48 | +0.45 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | -0.52 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[KDM4B]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[CCNI]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PPFIA1]] | -0.48 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[TMEM50B]] | -0.48 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[FBXO42]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[VKORC1]] | -0.47 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[PPP1R21]] | -0.46 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[VEGFB]] | -0.46 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[PPP2R5B]] | -0.46 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[RAB40C]] | -0.46 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[P4HA1]] | -0.46 | -0.46 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TLR4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PLPP4]] | C | PLPP4 activity raises TLR4's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 2.70× lower at baseline in the lines without PLPP4 | 0.013 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6; co-absent with the target |
| [[MILR1]] | C | MILR1 activity raises TLR4's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 2.20× lower at baseline in the lines without MILR1 | 0.025 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1; co-absent with the target |
| [[LINC02930]] | C | LINC02930 activity raises TLR4's level | lines that do not express LINC02930 (33) vs lines expressing it (17) | 2.07× lower at baseline in the lines without LINC02930 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000232053, GYPC, PLPP4; co-absent with the target |
| [[SRPX2]] | C | SRPX2 activity raises TLR4's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 2.02× lower at baseline in the lines without SRPX2 | 0.040 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CBFA2T2]] | B | TLR4 activity raises CBFA2T2's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 1.39× lower at baseline in the lines without TLR4 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP |
| [[MAML2]] | B | TLR4 activity raises MAML2's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 2.43× lower at baseline in the lines without TLR4 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP |
| [[RPS2]] | B | TLR4 activity lowers RPS2's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 1.42× higher at baseline in the lines without TLR4 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP |
| [[UTP20]] | B | TLR4 activity lowers UTP20's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 1.42× higher at baseline in the lines without TLR4 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP |
| [[MILR1]] | C | TLR4 activity raises MILR1's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 2.33× lower at baseline in the lines without TLR4 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP; co-absent with the target |
| [[PLPP4]] | C | TLR4 activity raises PLPP4's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 2.64× lower at baseline in the lines without TLR4 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP; co-absent with the target |
| [[IL7R]] | C | TLR4 activity raises IL7R's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 3.38× lower at baseline in the lines without TLR4 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP; co-absent with the target |
| [[LINC03004]] | C | TLR4 activity raises LINC03004's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 1.75× lower at baseline in the lines without TLR4 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP; co-absent with the target |
| [[LINC02930]] | C | TLR4 activity raises LINC02930's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 1.60× lower at baseline in the lines without TLR4 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP; co-absent with the target |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.9, 12.5); signed map (17.2, 40.2). **Vector** length 38.3, 8.06% of its response variance represented; |z| ≥ 3 in 441 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +1.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -1.5 | -3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.1 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | -2.8 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | toll like receptor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.1 — chr9:117,704,175-117,724,735 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hToll, CD284, TLR-4, ARMD10 |
| Gene groups (HGNC) | CD molecules; Toll like receptors |
| Reactome | 41 pathways, smallest: TRIF-mediated programmed cell death; Regulation of TBK1, IKKε (IKBKE)-mediated activation of IRF3, IRF7; Caspase activation via Death Receptors in the presence of ligand |
| Matched by | ensembl_id |

**Function**, from UniProt [O00206](https://www.uniprot.org/uniprotkb/O00206) (Toll-like receptor 4):

> Transmembrane receptor that functions as a pattern recognition receptor recognizing pathogen- and damage-associated molecular patterns (PAMPs and DAMPs) to induce innate immune responses via downstream signaling pathways. At the plasma membrane, cooperates with LY96 to mediate the innate immune response to bacterial lipopolysaccharide (LPS). Also involved in LPS-independent inflammatory responses triggered by free fatty acids, such as palmitate, and Ni(2+). Mechanistically, acts via MYD88, …

**Summary**, from NCBI Gene [7099](https://www.ncbi.nlm.nih.gov/gene/7099):

> The protein encoded by this gene is a member of the Toll-like receptor (TLR) family which plays a fundamental role in pathogen recognition and activation of innate immunity. TLRs are highly conserved from Drosophila to humans and share structural and functional similarities. They recognize pathogen-associated molecular patterns that are expressed on infectious agents, and mediate the production of cytokines necessary for the development of effective immunity. The various TLRs exhibit different …

**Accessions** — [HGNC:11850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11850) · Entrez [7099](https://www.ncbi.nlm.nih.gov/gene/7099) · UniProt [O00206](https://www.uniprot.org/uniprotkb/O00206) · Ensembl [ENSG00000136869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136869)

## Data

Gene col 5925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5925); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5925]; `tensor/DDL_lfc|DDL_z.npy` [5925]; `embed/gene_vectors.npy` [5925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5925 or target_col == 5925). Every well: [[TLR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
