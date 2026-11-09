---
symbol: "RFX5"
type: "gene"
col: 6734
ensembl_id: "ENSG00000143390"
name: "regulatory factor X5"
location: "1q21.3"
module: 25
arm: "+"
pooled_cpm: 11.3
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# RFX5

*regulatory factor X5* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.56× (z +15.3, q 0e+00, up in 14 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +8.2, q 4e-14, up in 23 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.648× (z -5.4, q 3e-05, down in 22 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.502× (z -4.5, q 0.001, down in 18 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOBEC3B]] (+0.59, fdr 1e-05), [[SRSF3]] (+0.56, fdr 1e-05), [[RBBP9]] (+0.55, fdr 1e-05); moves opposite to [[DRD4]] (-0.56, fdr 1e-05), [[RPL18]] (-0.54, fdr 2e-05, ⚠ RPL18 in the vector space only through flagged drug-doses), [[RPLP2]] (-0.53, fdr 2e-05), [[FAU]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RNF207]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.56×** | +15.3 | 0e+00 | 14/14 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.28×** | +13.7 | 2e-40 | 24/25 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +12.3 | 2e-32 | 30/33 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +8.2 | 4e-14 | 23/44 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +7.5 | 9e-12 | 27/46 (NCI-H1573, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +7.1 | 1e-10 | 28/44 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +5.0 | 5e-05 | 17/38 (MIA PaCa-2, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.0 | 5e-05 | 3/47 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.47×** | +4.8 | 1e-04 | 15/44 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.5 | 4e-04 | 14/47 (RKO, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.005 | 12/46 (HT-29, SW 900, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +3.9 | 0.005 | 11/46 (LoVo, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.007 | 18/46 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.34×** | +3.5 | 0.017 | 9/36 (C-33 A, SW 900, …) | rises with dose | position effect removed |
| [[Trifluridine (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.020 | 11/46 (SHP-77, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Cyclosporin A (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.051 | 5/44 (A-172, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6734.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.648×** | -5.4 | 3e-05 | 22/46 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.685×** | -4.7 | 7e-04 | 23/44 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.502×** | -4.5 | 0.001 | 18/39 (A-172, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.701×** | -4.2 | 0.004 | 15/45 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.728×** | -4.0 | 0.008 | 16/46 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.661×** | -3.7 | 0.021 | 16/46 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.820×** | -3.5 | 0.037 | 12/46 (LOX-IMVI, SW 900, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.771×** | -3.3 | 0.079 | 16/46 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.776×** | -3.2 | 0.097 | 15/46 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 22.2 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0778× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~73% of this change |
| [[A-427 (line)]] | wt | 25.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0895× (z -8.6) |
| [[Hs 766T (line)]] | wt | 6.58 | 0 | 2 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0831× (z -9.1) |
| [[A-172 (line)]] | wt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 8.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 5.34 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0898× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -8.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOBEC3B]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SRSF3]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[RBBP9]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[HUWE1]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[BAHCC1]] | +0.55 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[CFL2]] | +0.54 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[OGFRL1]] | +0.54 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[HLA-H]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[FECH]] | +0.54 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TRIM68]] | +0.53 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[PARP3]] | +0.53 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[TAPBP]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 | STRING 439 |

## Genes that move opposite

*51 of its nearest partners move opposite, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRD4]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | -0.54 | -0.46 / -0.48 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPLP2]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[FAU]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[RPL9]] ⚠ | -0.52 | -0.46 / -0.50 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ANKS3]] | -0.52 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[RPS3]] ⚠ | -0.52 | -0.41 / -0.51 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | -0.52 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[UQCRH]] | -0.52 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[RPL37A]] ⚠ | -0.52 | -0.46 / -0.48 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS13]] ⚠ | -0.51 | -0.43 / -0.50 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DYNC2I1]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[PRKRIP1]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[RPL36]] | -0.51 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[COMMD6]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[MIR4458HG]] | -0.51 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ATP5MJ]] | -0.51 | -0.50 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF207]] | B | RNF207 activity raises RFX5's level | lines that do not express RNF207 (6) vs lines expressing it (44) | 1.64× lower at baseline in the lines without RNF207 | 0.097 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.506). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-37.8, -23.1); signed map (17.4, -38.9). **Vector** length 90.5, 18.5% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +12.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.2 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.0 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.7 | +2.6 |
| fall | [[EX229 (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -5.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -4.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.3 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | regulatory factor X5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,340,640-151,347,326 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Regulatory factor X family |
| Matched by | ensembl_id |

**Function**, from UniProt [P48382](https://www.uniprot.org/uniprotkb/P48382) (DNA-binding protein RFX5):

> Activates transcription from class II MHC promoters. Recognizes X-boxes. Mediates cooperative binding between RFX and NF-Y. RFX binds the X1 box of MHC-II promoters.

**Summary**, from NCBI Gene [5993](https://www.ncbi.nlm.nih.gov/gene/5993):

> A lack of MHC-II expression results in a severe immunodeficiency syndrome called MHC-II deficiency, or the bare lymphocyte syndrome (BLS; MIM 209920). At least 4 complementation groups have been identified in B-cell lines established from patients with BLS. The molecular defects in complementation groups B, C, and D all lead to a deficiency in RFX, a nuclear protein complex that binds to the X box of MHC-II promoters. The lack of RFX binding activity in complementation group C results from …

**Accessions** — [HGNC:9986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9986) · Entrez [5993](https://www.ncbi.nlm.nih.gov/gene/5993) · UniProt [P48382](https://www.uniprot.org/uniprotkb/P48382) · Ensembl [ENSG00000143390](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143390)

## Data

Gene col 6734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6734); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6734]; `tensor/DDL_lfc|DDL_z.npy` [6734]; `embed/gene_vectors.npy` [6734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6734 or target_col == 6734). Every well: [[RFX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
