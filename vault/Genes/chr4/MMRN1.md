---
symbol: "MMRN1"
type: "gene"
col: 6220
ensembl_id: "ENSG00000138722"
name: "multimerin 1"
location: "4q22.1"
module: 9
arm: "+"
pooled_cpm: 3.29
n_lines_expressing: 7
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 10
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MMRN1

*multimerin 1* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.73× (z +12.3, q 6e-32, up in 0 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.479× (z -4.2, q 0.016, down in 0 of 5 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (NCI-H661 0.0435×); [[Belinostat (drug)]] 5 µM in 1 line (A-427 0.183×; ⚠ cell-cycle shift, explains ~36% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01203]] (+0.71, fdr 7e-06), [[MIR99AHG]] (+0.69, fdr 7e-06), [[ERBB4]] (+0.67, fdr 3e-05); moves opposite to [[KRBOX4]] (-0.44, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GCG]] → it (grade C ⚠); 10 go from it, the strongest it → [[SALL4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6220.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.73×** | +12.3 | 6e-32 | 0/4 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.70×** | +10.2 | 4e-22 | 1/4 (A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.59×** | +9.6 | 1e-19 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.64×** | +8.9 | 5e-17 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.11×** | +5.6 | 2e-06 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.96×** | +5.3 | 1e-05 | 2/5 (A-427, Hs 766T) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +5.2 | 2e-05 | 0/4 | top dose only | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.63×** | +5.2 | 2e-05 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.62×** | +5.2 | 2e-05 | 1/5 (A-427) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +4.8 | 9e-05 | 0/5 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.51×** | +4.4 | 6e-04 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +4.2 | 0.001 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.2 | 0.001 | 0/5 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.11×** | +4.1 | 0.001 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.04×** | +4.0 | 0.003 | 0/5 | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.64×** | +3.9 | 0.004 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.98×** | +3.8 | 0.005 | 1/4 (NCI-H1792) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.48×** | +3.6 | 0.009 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.028 | 0/5 | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.030 | 1/5 (NCI-H1792) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Saquinavir (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.033 | 0/4 | inconsistent across doses |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.87×** | +3.2 | 0.035 | 0/4 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +2.9 | 0.087 | 0/5 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.75×** | +2.9 | 0.087 | 0/4 | inconsistent across doses | position effect removed |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.67×** | +2.8 | 0.090 | 0/4 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6220.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (NCI-H661 0.0435×); [[Belinostat (drug)]] 5 µM in 1 line (A-427 0.183×; ⚠ cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.479×** | -4.2 | 0.016 | 0/5 | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.569× | -3.2 | 0.36 | 0/5 | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.559× | -3.1 | 0.41 | 0/5 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 93.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.183× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H661 (line)]] | alt | 42.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0435× (z -9.0) |
| [[A-172 (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.215 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.395 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.244 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01203]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[MIR99AHG]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ERBB4]] | +0.67 | +0.45 / +0.73 | both halves | 3e-05 | **novel candidate** |
| [[ZFHX4-AS1]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[UNC5C]] | +0.65 | +0.57 / +0.66 | both halves | 8e-06 |  |
| [[ANKS1B]] | +0.63 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[LINC02643]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[GCG]] | +0.61 | +0.74 / +0.36 | both halves | 1e-04 | **novel candidate** |
| [[CTNNA2]] | +0.61 | +0.42 / +0.69 | both halves | 4e-05 |  |
| [[KLHL13]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CDH10]] | +0.59 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[EPHA5]] | +0.58 | +0.42 / +0.67 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRBOX4]] | -0.44 | -0.30 / -0.34 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCG]] | C | GCG activity raises MMRN1's level | lines that do not express GCG (46) vs lines expressing it (4) | 8.57× lower at baseline in the lines without GCG | 0.061 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, LINC01205, APOB; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SALL4]] | B | MMRN1 activity raises SALL4's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 6.60× lower at baseline in the lines without MMRN1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5 |
| [[ERBB4]] | C | MMRN1 activity raises ERBB4's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 14.21× lower at baseline in the lines without MMRN1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |
| [[LINC01205]] | C | MMRN1 activity raises LINC01205's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 2.81× lower at baseline in the lines without MMRN1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |
| [[CDH18]] | C | MMRN1 activity raises CDH18's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 4.96× lower at baseline in the lines without MMRN1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |
| [[LINC02008]] | C | MMRN1 activity raises LINC02008's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 2.43× lower at baseline in the lines without MMRN1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |
| [[ZFHX4-AS1]] | C | MMRN1 activity raises ZFHX4-AS1's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 5.15× lower at baseline in the lines without MMRN1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |
| [[UNC5C]] | C | MMRN1 activity raises UNC5C's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 2.24× lower at baseline in the lines without MMRN1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |
| [[GPC3]] | C | MMRN1 activity raises GPC3's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 4.93× lower at baseline in the lines without MMRN1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |
| [[GCG]] | C | MMRN1 activity raises GCG's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 3.59× lower at baseline in the lines without MMRN1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |
| [[LINC01203]] | C | MMRN1 activity raises LINC01203's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 4.26× lower at baseline in the lines without MMRN1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.0, 32.7); signed map (39.2, 35.1). **Vector** length 14.9, 4.69% of its response variance represented; |z| ≥ 3 in 101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.1 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.1 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.0 | +10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.9 | +12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +0.9 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.3 | +2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.3 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.3 | +3.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.2 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.5 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.4 | -0.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.3 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.3 | -0.4 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.3 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.3 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | multimerin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:89,879,532-89,954,629 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ECM, EMILIN4, GPIa*; previously MMRN |
| Gene groups (HGNC) | EMI domain containing; C1q domain containing |
| Reactome | 5 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13201](https://www.uniprot.org/uniprotkb/Q13201) (Multimerin-1):

> Carrier protein for platelet (but not plasma) factor V/Va. Plays a role in the storage and stabilization of factor V in platelets. Upon release following platelet activation, may limit platelet and plasma factor Va-dependent thrombin generation. Ligand for integrin alpha-IIb/beta-3 and integrin alpha-V/beta-3 on activated platelets, and may function as an extracellular matrix or adhesive protein.

**Summary**, from NCBI Gene [22915](https://www.ncbi.nlm.nih.gov/gene/22915):

> Multimerin is a massive, soluble protein found in platelets and in the endothelium of blood vessels. It is comprised of subunits linked by interchain disulfide bonds to form large, variably sized homomultimers. Multimerin is a factor V/Va-binding protein and may function as a carrier protein for platelet factor V. It may also have functions as an extracellular matrix or adhesive protein. Recently, patients with an unusual autosomal-dominant bleeding disorder (factor V Quebec) were found to have …

**Accessions** — [HGNC:7178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7178) · Entrez [22915](https://www.ncbi.nlm.nih.gov/gene/22915) · UniProt [Q13201](https://www.uniprot.org/uniprotkb/Q13201) · Ensembl [ENSG00000138722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138722)

## Data

Gene col 6220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6220); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6220]; `tensor/DDL_lfc|DDL_z.npy` [6220]; `embed/gene_vectors.npy` [6220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6220 or target_col == 6220). Every well: [[MMRN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMRN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
