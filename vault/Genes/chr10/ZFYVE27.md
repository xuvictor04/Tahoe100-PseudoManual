---
symbol: "ZFYVE27"
type: "gene"
col: 7880
ensembl_id: "ENSG00000155256"
name: "zinc finger FYVE-type containing 27"
location: "10q24.2"
module: 15
arm: "+"
pooled_cpm: 36.98
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ZFYVE27

*zinc finger FYVE-type containing 27* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +8.9, q 5e-16, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.572× (z -9.4, q 2e-18, down in 28 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.724× (z -5.7, q 2e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSC22D4]] (+0.66, fdr 7e-06), [[GUCD1]] (+0.65, fdr 1e-05), [[TAF11]] (+0.63, fdr 1e-05); moves opposite to [[ZMYM4]] (-0.62, fdr 1e-05), [[NEK1]] (-0.61, fdr 1e-05), [[PBRM1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7880.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +8.9 | 5e-16 | 34/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.2 | 2e-10 | 29/46 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +7.0 | 6e-10 | 31/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.5 | 5e-06 | 24/46 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 3e-04 | 22/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 4e-04 | 27/48 (HEC-1-A, SHP-77, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.20×** | +4.6 | 4e-04 | 16/48 (LoVo, HT-29, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 4e-04 | 25/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.001 | 24/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 22/48 (SHP-77, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.003 | 17/48 (HEC-1-A, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.064 | 14/48 (A-427, C-33 A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.1 | 0.083 | 0/49 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.085 | 14/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7880.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.572×** | -9.4 | 2e-18 | 28/38 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.617×** | -8.5 | 5e-15 | 37/46 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.724×** | -5.7 | 2e-06 | 26/48 (COLO 205, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.747×** | -4.9 | 1e-04 | 24/48 (NCI-H2347, COLO 205, …) | two highest doses | composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.771×** | -4.6 | 5e-04 | 24/48 (RKO, NCI-H1573, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.866× | -3.6 | 0.031 | 12/48 (LOX-IMVI, NCI-H2347, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.827×** | -3.3 | 0.065 | 19/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.830×** | -3.3 | 0.065 | 13/48 (CHP-212, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **0.770×** | -3.3 | 0.065 | 12/48 (SNU-1, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7880. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 40.6 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.1 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 28.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[OTS514 (drug)]] 5 µM 0.0570× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 28.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 36.7 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -14.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 41.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 51.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.443× (z -8.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -9.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 49.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0800× (z -11.2) |
| [[COLO 205 (line)]] | alt | 60.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.299× (z -8.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[H4 (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -10.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -9.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 36.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0969× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[LoVo (line)]] | wt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 43.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 34.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 37.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 40.0 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.236× (z -9.0) |
| [[SW 900 (line)]] | alt | 47.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -11.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 47.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 48.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7880), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D4]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[GUCD1]] | +0.65 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[TAF11]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[DHRS1]] | +0.62 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[WDR20]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[LINC00115]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[FAHD2A]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CERS5]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[RAB5B]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[IFI27L1]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[STARD3]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 | STRING 895 |
| [[ZNF394]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM4]] | -0.62 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[NEK1]] | -0.61 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[PBRM1]] | -0.60 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ZNF22]] | -0.60 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[TBC1D19]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[PCNX2]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[KLHL9]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[WDR7]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[AGGF1]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ASF1A]] | -0.55 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[FKTN]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.54 | -0.58 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZFYVE27's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.8, 24.6); signed map (-22.9, 1.7). **Vector** length 88.5, 18.7% of its response variance represented; |z| ≥ 3 in 844 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | -0.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -6.6 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -5.3 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger FYVE-type containing 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:97,737,121-97,760,907 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32919, SPG33 |
| Gene groups (HGNC) | Zinc fingers FYVE-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T4F4](https://www.uniprot.org/uniprotkb/Q5T4F4) (Protrudin):

> Molecular tethering protein, which plays a role in the formation of membrane contact sites between the endoplasmic reticulum and late endosomes/lysosomes. Promotes neurite formation by tethering endosomes to the endoplasmic reticulum membrane: interacts with Rab7-positive late endosomes, acting as a bridge to form endoplasmic reticulum membrane-endosome contact sites. Acts in cooperation with vesicle-associated membrane protein-associated protein (VAPA or VAPB), thereby facilitating loading of …

**Summary**, from NCBI Gene [118813](https://www.ncbi.nlm.nih.gov/gene/118813):

> This gene encodes a protein with several transmembrane domains, a Rab11-binding domain and a lipid-binding FYVE finger domain. The encoded protein appears to promote neurite formation. A mutation in this gene has been reported to be associated with hereditary spastic paraplegia, however the pathogenicity of the mutation, which may simply represent a polymorphism, is unclear. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:26559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26559) · Entrez [118813](https://www.ncbi.nlm.nih.gov/gene/118813) · UniProt [Q5T4F4](https://www.uniprot.org/uniprotkb/Q5T4F4) · Ensembl [ENSG00000155256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155256)

## Data

Gene col 7880: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7880); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7880, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7880]; `tensor/DDL_lfc|DDL_z.npy` [7880]; `embed/gene_vectors.npy` [7880]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7880 or target_col == 7880). Every well: [[ZFYVE27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFYVE27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
