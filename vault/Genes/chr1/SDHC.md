---
symbol: "SDHC"
type: "gene"
col: 6704
ensembl_id: "ENSG00000143252"
name: "succinate dehydrogenase complex subunit C"
location: "1q23.3"
module: 156
arm: "+"
pooled_cpm: 21.96
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# SDHC

*succinate dehydrogenase complex subunit C* — 1q23.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (13 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.515× (z -7.8, q 4e-12, down in 36 of 43 measured lines) ⚠ toxic; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 0.767× (z -3.1, q 0.089, down in 14 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.190×, HepG2/C3A 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 0.185×, PANC-1 0.300×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.185×, LS 180 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.186×); [[Imiquimod (maleate) (drug)]] 0.05 µM in 1 line (SW48 0.0835×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0976×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG8]] (+0.63, fdr 1e-05), [[ALKBH1]] (+0.62, fdr 1e-05), [[PYM1]] (+0.61, fdr 1e-05); moves opposite to [[MYLIP]] (-0.59, fdr 1e-05), [[OSR2]] (-0.54, fdr 3e-05), [[MLF1]] (-0.54, fdr 2e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZMIZ1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6704.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.22× | +3.4 | 0.46 | 17/47 (A-172, AsPC-1, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6704.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.190×, HepG2/C3A 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 0.185×, PANC-1 0.300×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.185×, LS 180 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.186×); [[Imiquimod (maleate) (drug)]] 0.05 µM in 1 line (SW48 0.0835×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0976×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.515×** | -7.8 | 4e-12 | 36/43 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.588×** | -6.5 | 2e-08 | 28/47 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.589×** | -6.4 | 2e-08 | 32/45 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.693×** | -4.5 | 0.001 | 25/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.705×** | -4.3 | 0.002 | 24/47 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | **0.708×** | -4.2 | 0.002 | 25/44 (CFPAC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.693×** | -4.1 | 0.003 | 21/35 (NCI-H1573, RPMI-7951, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.713×** | -4.1 | 0.003 | 22/46 (SW1417, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.744×** | -3.5 | 0.034 | 20/45 (NCI-H23, SNU-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.748×** | -3.4 | 0.036 | 20/46 (A-427, J82, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.757×** | -3.4 | 0.036 | 17/46 (SNU-1, NCI-H1792, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.767×** | -3.1 | 0.089 | 14/47 (NCI-H460, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.778×** | -3.1 | 0.093 | 15/46 (NCI-H460, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.779×** | -3.0 | 0.093 | 14/47 (A-172, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.839× | -3.0 | 0.093 | 14/47 (CHP-212, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6704. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.4 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H23 (line)]] | alt | 45.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 24.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[HepG2_C3A (line)]] | wt | 15.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 25.5 | 0 | 2 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.186× (z -10.6) |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 16.8 | 0 | 2 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0793× (z -10.8) ⚠ toxic · without an alert: [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0835× (z -10.2) |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM 0.0620× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.234× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~68% of this change |
| [[HOP62 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0976× (z -9.2) |
| [[LoVo (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.208× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[RKO (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.212× (z -8.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6704), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG8]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[PYM1]] | +0.61 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[UQCC1]] | +0.60 | +0.58 / +0.57 | both halves | 9e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[CWF19L1]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[DGUOK]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[MCM3AP]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[SPRYD4]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[TRMT61B]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[MRRF]] | +0.58 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[TFCP2]] | +0.58 | +0.65 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLIP]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[OSR2]] | -0.54 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[MLF1]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[USP2]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PEAK1]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SSBP3]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ATP8A1]] | -0.51 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[NOS1AP]] | -0.50 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[MPC2]] | -0.50 | -0.38 / -0.46 | both halves | 6e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[IFRD1]] | -0.50 | -0.43 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMIZ1]] | C | ZMIZ1 activity lowers SDHC's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 1.71× higher at baseline in the lines without ZMIZ1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.9, 3.9); signed map (-8.0, -21.9). **Vector** length 70.1, 12.9% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +1.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.6 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.6 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.6 | +1.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | -4.7 | -7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -2.5 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.9 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | succinate dehydrogenase complex subunit C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,314,381-161,363,206 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CYB560, cybL; previously PGL3 |
| Gene groups (HGNC) | Mitochondrial complex II: succinate dehydrogenase subunits |
| Hallmark sets | FATTY_ACID_METABOLISM, GLYCOLYSIS, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle); Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99643](https://www.uniprot.org/uniprotkb/Q99643) (Succinate dehydrogenase cytochrome b560 subunit, mitochondrial):

> Membrane-anchoring subunit of succinate dehydrogenase (SDH) that is involved in complex II of the mitochondrial electron transport chain and is responsible for transferring electrons from succinate to ubiquinone (coenzyme Q). SDH also oxidizes malate to the non-canonical enol form of oxaloacetate, enol-oxaloacetate (By similarity). Enol-oxaloacetate, which is a potent inhibitor of the succinate dehydrogenase activity, is further isomerized into keto-oxaloacetate (By similarity).

**Summary**, from NCBI Gene [6391](https://www.ncbi.nlm.nih.gov/gene/6391):

> This gene encodes one of four nuclear-encoded subunits that comprise succinate dehydrogenase, also known as mitochondrial complex II, a key enzyme complex of the tricarboxylic acid cycle and aerobic respiratory chains of mitochondria. The encoded protein is one of two integral membrane proteins that anchor other subunits of the complex, which form the catalytic core, to the inner mitochondrial membrane. There are several related pseudogenes for this gene on different chromosomes. Mutations in …

**Accessions** — [HGNC:10682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10682) · Entrez [6391](https://www.ncbi.nlm.nih.gov/gene/6391) · UniProt [Q99643](https://www.uniprot.org/uniprotkb/Q99643) · Ensembl [ENSG00000143252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143252)

## Data

Gene col 6704: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6704); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6704, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6704]; `tensor/DDL_lfc|DDL_z.npy` [6704]; `embed/gene_vectors.npy` [6704]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6704 or target_col == 6704). Every well: [[SDHC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
