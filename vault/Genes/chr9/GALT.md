---
symbol: "GALT"
type: "gene"
col: 13151
ensembl_id: "ENSG00000213930"
name: "galactose-1-phosphate uridylyltransferase"
location: "9p13.3"
module: 14
arm: "+"
pooled_cpm: 5.82
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 11
n_dd_up_clean: 18
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# GALT

*galactose-1-phosphate uridylyltransferase* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.75× (z +7.3, q 1e-10, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.471× (z -9.9, q 4e-20, down in 26 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.481× (z -9.6, q 3e-19, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC24]] (+0.62, fdr 7e-06), [[KMT2E]] (+0.62, fdr 1e-05), [[IL11RA]] (+0.61, fdr 7e-06, ⚠ same locus), [[RAB24]] (+0.61, fdr 1e-05); moves opposite to [[TMEM181]] (-0.61, fdr 8e-06), [[SLC20A2]] (-0.59, fdr 1e-05), [[GART]] (-0.58, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BBS5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +7.3 | 1e-10 | 24/46 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +6.7 | 8e-09 | 20/48 (RKO, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +6.5 | 1e-08 | 24/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +4.8 | 2e-04 | 16/47 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.5 | 6e-04 | 4/12 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +4.5 | 6e-04 | 12/46 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 6e-04 | 8/44 (LoVo, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.2 | 0.002 | 5/18 (J82, A498, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +4.2 | 0.002 | 9/47 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.004 | 8/46 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.006 | 11/43 (RKO, NCI-H23, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.007 | 4/44 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.012 | 8/47 (NCI-H23, A498, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.017 | 8/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.033 | 1/47 (KATO III) | rises with dose | position effect removed |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.035 | 6/43 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.067 | 11/44 (BT-474, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13151.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.471×** | -9.9 | 4e-20 | 26/43 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.481×** | -9.6 | 3e-19 | 28/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.499×** | -9.1 | 2e-17 | 29/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.613×** | -6.4 | 2e-08 | 22/45 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.717×** | -4.3 | 0.002 | 15/47 (SW 900, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.729×** | -4.1 | 0.004 | 12/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.746×** | -3.8 | 0.011 | 13/45 (C32, SNU-423, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.766×** | -3.5 | 0.035 | 11/47 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.767×** | -3.5 | 0.035 | 12/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.831×** | -3.4 | 0.039 | 11/46 (RPMI-7951, SHP-77, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.775×** | -3.1 | 0.087 | 12/46 (SNU-1, C32, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.791× | -3.0 | 0.10 | 14/47 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | 0.640× | -3.0 | 0.10 | 7/40 (HS-578T, C-33 A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.80 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 11.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.68× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 3.50 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0572× (z -10.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 4.15 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0871× (z -8.9) |
| [[LoVo (line)]] | wt | 5.56 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0838× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 4.45 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0482× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 4.51 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC24]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[KMT2E]] | +0.62 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[IL11RA]] | +0.61 | +0.62 / +0.62 | both halves | 7e-06 | STRING 930; ⚠ same locus (1.1 kb, same strand: neighbours can correlate without regulation) |
| [[RAB24]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[RHOV]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[YY1AP1]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[NFKBIA]] | +0.59 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[CLN8-AS1]] | +0.59 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ZNF428]] | +0.59 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ZNF14]] | +0.58 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[SPACA9]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ATG4D]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM181]] | -0.61 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[SLC20A2]] | -0.59 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[GART]] | -0.58 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[PRMT3]] | -0.57 | -0.38 / -0.61 | both halves | 7e-05 |  |
| [[SLFNL1-AS1]] | -0.54 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[UGGT2]] | -0.54 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[KLHL29]] | -0.54 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[LMBR1]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZNF800]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[PKP4]] | -0.52 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[TIMM23B-AGAP6]] | -0.51 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[SPON1-AS1]] | -0.51 | -0.23 / -0.62 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BBS5]] | B | BBS5 activity raises GALT's level | lines that do not express BBS5 (6) vs lines expressing it (44) | 1.25× lower at baseline in the lines without BBS5 | 0.051 | ⚠ within organs, on part of the lines; also absent: GGT7, HLTF, FERMT2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers GALT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.2, -37.0); signed map (-9.6, 2.9). **Vector** length 50.9, 6.18% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.6 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +4.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.2 | +3.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +4.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -4.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | galactose-1-phosphate uridylyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,638,133-34,651,035 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Histidine triad superfamily |
| Reactome | 5 pathways, smallest: Galactose catabolism; Diseases associated with glycosylation precursor biosynthesis; Diseases of glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P07902](https://www.uniprot.org/uniprotkb/P07902) (Galactose-1-phosphate uridylyltransferase):

> Plays an important role in galactose metabolism.

**Summary**, from NCBI Gene [2592](https://www.ncbi.nlm.nih.gov/gene/2592):

> Galactose-1-phosphate uridyl transferase (GALT) catalyzes the second step of the Leloir pathway of galactose metabolism, namely the conversion of UDP-glucose + galactose-1-phosphate to glucose-1-phosphate + UDP-galactose. The absence of this enzyme results in classic galactosemia in humans and can be fatal in the newborn period if lactose is not removed from the diet. The pathophysiology of galactosemia has not been clearly defined. Two transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:4135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4135) · Entrez [2592](https://www.ncbi.nlm.nih.gov/gene/2592) · UniProt [P07902](https://www.uniprot.org/uniprotkb/P07902) · Ensembl [ENSG00000213930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213930)

## Data

Gene col 13151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13151); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13151]; `tensor/DDL_lfc|DDL_z.npy` [13151]; `embed/gene_vectors.npy` [13151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13151 or target_col == 13151). Every well: [[GALT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
