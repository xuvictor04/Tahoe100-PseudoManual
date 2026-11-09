---
symbol: "OGT"
type: "gene"
col: 7157
ensembl_id: "ENSG00000147162"
name: "O-linked N-acetylglucosamine (GlcNAc) transferase"
location: "Xq13.1"
module: 20
arm: "+"
pooled_cpm: 188.89
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# OGT

*O-linked N-acetylglucosamine (GlcNAc) transferase* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.88× (z +7.6, q 1e-11, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.606× (z -6.1, q 5e-07, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.704× (z -6.0, q 5e-07, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LENG8]] (+0.64, fdr 1e-05), [[SNHG22]] (+0.60, fdr 4e-05), [[AP2B1]] (+0.59, fdr 1e-05); moves opposite to [[MRPL36]] (-0.57, fdr 3e-05), [[ISCA2]] (-0.54, fdr 9e-05), [[EMC6]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.88×** | +7.6 | 1e-11 | 46/48 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +5.2 | 5e-05 | 44/48 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.3 | 0.003 | 34/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.96×** | +4.2 | 0.003 | 38/48 (RPMI-7951, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.86×** | +3.9 | 0.009 | 33/49 (AsPC-1, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.023 | 30/48 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +3.3 | 0.077 | 31/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.088 | 31/48 (A549, SW480, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7157.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.606×** | -6.1 | 5e-07 | 41/48 (RPMI-7951, PANC-1, …) | all doses, flat | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.704×** | -6.0 | 5e-07 | 31/49 (A549, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.675×** | -4.8 | 4e-04 | 38/48 (RPMI-7951, PANC-1, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.728×** | -3.9 | 0.016 | 39/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.723×** | -3.8 | 0.017 | 33/47 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.738×** | -3.7 | 0.021 | 33/48 (PANC-1, H4, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.809×** | -3.6 | 0.022 | 34/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.743×** | -3.6 | 0.022 | 34/48 (CFPAC-1, SW 1271, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Arbutin (drug)]] 5 µM |  | 0.770× | -3.1 | 0.14 | 33/48 (hTERT-HPNE, NCI-H2347, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.839× | -3.0 | 0.14 | 20/48 (hTERT-HPNE, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 135 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +11.4) | — |
| [[RPMI-7951 (line)]] | alt | 415 | 1 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.45× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 216 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +16.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 250 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.405× (z -9.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -9.3) |
| [[RKO (line)]] | wt | 185 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -10.5) |
| [[A549 (line)]] | wt | 160 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -14.4) |
| [[C32 (line)]] | wt | 89.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.78× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 90.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -11.3) ⚠ toxic |
| [[KATO III (line)]] | alt | 194 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 313 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -11.5) |
| [[LS 180 (line)]] | wt | 160 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 236 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 178 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 122 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +10.5) | — |
| [[SW48 (line)]] | wt | 233 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +9.4) | — |
| [[SW480 (line)]] | alt | 301 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +8.7) | — |
| [[A-172 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 126 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 143 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 162 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 203 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 137 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 184 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 208 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 214 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LENG8]] | +0.64 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[SNHG22]] | +0.60 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[AP2B1]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[EIF2D]] | +0.58 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[SLC38A1]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[RPS3A]] | +0.54 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CERS2]] | +0.54 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[FAM219B]] | +0.54 | +0.59 / +0.40 | both halves | 4e-05 |  |
| [[DHFR]] | +0.53 | +0.30 / +0.63 | both halves | 2e-04 |  |
| [[CTSZ]] | +0.53 | +0.37 / +0.54 | both halves | 7e-05 |  |
| [[MTHFD2]] | +0.53 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[RPSA]] | +0.53 | +0.41 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL36]] | -0.57 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[ISCA2]] | -0.54 | -0.37 / -0.58 | both halves | 9e-05 |  |
| [[EMC6]] | -0.54 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[NUDT16L1]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[KRTCAP2]] | -0.51 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[UQCR10]] ⚠ | -0.51 | -0.35 / -0.56 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[POLR2J]] ⚠ | -0.51 | -0.34 / -0.58 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF503]] | -0.51 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[EID2]] | -0.50 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[C16orf91]] | -0.50 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[IL10RB]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TIMM17B]] ⚠ | -0.50 | -0.46 / -0.47 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC2B]] | -0.49 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[TOPORS]] | -0.49 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[CDKN2AIP]] | -0.49 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises OGT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.495). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-46.6, -12.0); signed map (-20.0, -31.8). **Vector** length 95.3, 32.8% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.7 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.5 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.2 | +0.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.4 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | +1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.1 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.0 |
|  | [[Thymol (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | O-linked N-acetylglucosamine (GlcNAc) transferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:71,533,087-71,575,892 (+) |
| Ensembl biotype | protein_coding |
| Also known as | O-GLCNAC, HRNT1, MGC22921, FLJ23071, OGT1 |
| Gene groups (HGNC) | O-linked N-acetylglucosaminyltransferases; Tetratricopeptide repeat domain containing; NSL histone acetyltransferase complex |
| Reactome | 12 pathways, smallest: RIPK1-mediated regulated necrosis; Regulation of necroptotic cell death; Formation of WDR5-containing histone-modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15294](https://www.uniprot.org/uniprotkb/O15294) (UDP-N-acetylglucosamine--peptide N-acetylglucosaminyltransferase 110 kDa subunit):

> Catalyzes the transfer of a single N-acetylglucosamine from UDP-GlcNAc to a serine or threonine residue in cytoplasmic and nuclear proteins resulting in their modification with a beta-linked N-acetylglucosamine (O-GlcNAc). Glycosylates a large and diverse number of proteins including histone H2B, AKT1, AMPK, ATG4B, CAPRIN1, EZH2, FNIP1, GSDMD, KRT7, LMNA, LMNB1, LMNB2, RPTOR, HOXA1, PFKL, KMT2E/MLL5, MAPT/TAU, TET2, RBL2, RET, NOD2 and HCFC1. Can regulate their cellular processes via cross-talk …

**Summary**, from NCBI Gene [8473](https://www.ncbi.nlm.nih.gov/gene/8473):

> This gene encodes a glycosyltransferase that catalyzes the addition of a single N-acetylglucosamine in O-glycosidic linkage to serine or threonine residues. Since both phosphorylation and glycosylation compete for similar serine or threonine residues, the two processes may compete for sites, or they may alter the substrate specificity of nearby sites by steric or electrostatic effects. The protein contains multiple tetratricopeptide repeats that are required for optimal recognition of …

**Accessions** — [HGNC:8127](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8127) · Entrez [8473](https://www.ncbi.nlm.nih.gov/gene/8473) · UniProt [O15294](https://www.uniprot.org/uniprotkb/O15294) · Ensembl [ENSG00000147162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147162)

## Data

Gene col 7157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7157); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7157]; `tensor/DDL_lfc|DDL_z.npy` [7157]; `embed/gene_vectors.npy` [7157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7157 or target_col == 7157). Every well: [[OGT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OGT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
