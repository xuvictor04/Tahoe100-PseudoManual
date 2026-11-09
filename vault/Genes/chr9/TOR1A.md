---
symbol: "TOR1A"
type: "gene"
col: 5912
ensembl_id: "ENSG00000136827"
name: "torsin family 1 member A"
location: "9q34.11"
module: 5
arm: "+"
pooled_cpm: 10.18
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TOR1A

*torsin family 1 member A* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +8.4, q 3e-14, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.420× (z -11.2, q 2e-26, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HCFC1]] (+0.73, fdr 7e-06), [[ARSB]] (+0.72, fdr 2e-05), [[PSME3]] (+0.71, fdr 7e-06); moves opposite to [[SEC22A]] (-0.68, fdr 7e-06), [[BCAT2]] (-0.66, fdr 1e-05), [[CDKN2D]] (-0.66, fdr 5e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CDA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5912.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +8.4 | 3e-14 | 31/44 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +8.1 | 2e-13 | 15/19 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.0 | 6e-10 | 18/32 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.9 | 5e-07 | 20/48 (NCI-H460, NCI-H2347, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +5.6 | 3e-06 | 17/28 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.9 | 1e-04 | 15/45 (LoVo, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.7 | 2e-04 | 17/48 (LS 180, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.6 | 3e-04 | 21/46 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.3 | 0.001 | 19/39 (SW48, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +4.2 | 0.001 | 13/41 (J82, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.9 | 0.004 | 13/40 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.007 | 8/46 (J82, NCI-H1573, …) | top dose only | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.73×** | +3.7 | 0.009 | 8/42 (HEC-1-A, A498, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.29×** | +3.3 | 0.037 | 8/47 (A498, KATO III, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.074 | 8/46 (LoVo, A498, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5912.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.420×** | -11.2 | 2e-26 | 36/47 (SHP-77, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.438×** | -10.7 | 3e-24 | 39/47 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.568×** | -10.4 | 7e-23 | 33/44 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.477×** | -9.6 | 1e-19 | 37/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.638×** | -8.2 | 2e-14 | 33/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.613×** | -6.3 | 2e-08 | 28/47 (KATO III, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.675×** | -5.1 | 3e-05 | 22/46 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.493×** | -4.8 | 1e-04 | 21/48 (C-33 A, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.738×** | -3.8 | 0.010 | 18/45 (A-427, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.792× | -3.0 | 0.14 | 9/47 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 15.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0497× (z -13.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -13.2) |
| [[A-427 (line)]] | wt | 9.82 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.158× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~61% of this change |
| [[AsPC-1 (line)]] | alt | 5.23 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0824× (z -9.6) |
| [[COLO 205 (line)]] | alt | 7.85 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0696× (z -10.0) |
| [[HOP62 (line)]] | alt | 9.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -8.6) |
| [[J82 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -8.9) |
| [[KATO III (line)]] | alt | 11.0 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.213× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.4) |
| [[PANC-1 (line)]] | alt | 7.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.3) |
| [[RKO (line)]] | wt | 26.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 7.89 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0914× (z -9.0) |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -12.0) |
| [[SW 900 (line)]] | alt | 7.56 | 0 | 1 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0605× (z -11.2) |
| [[A-172 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | +0.73 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[ARSB]] | +0.72 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[PSME3]] | +0.71 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.71 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[KMT2D]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[CRPPA]] | +0.68 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[PIGW]] | +0.68 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD40]] | +0.68 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TLCD3A]] | +0.68 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[EPM2A]] | +0.67 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[MSANTD7]] | +0.67 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[RCC2]] | +0.67 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC22A]] | -0.68 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[BCAT2]] | -0.66 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.66 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[CFDP1]] | -0.65 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[SYP]] | -0.65 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[SLC17A5]] | -0.63 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.62 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[NBEAL1]] | -0.62 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[AFMID]] | -0.62 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[GOLGA4]] | -0.61 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[TOMM20]] | -0.61 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[PIGH]] | -0.61 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDA]] | B | CDA activity lowers TOR1A's level | lines that do not express CDA (16) vs lines expressing it (34) | 1.28× higher at baseline in the lines without CDA | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[TOP2A]] | B | TOP2A activity lowers TOR1A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HENMT1]] | B | HENMT1 activity lowers TOR1A's level | lines that do not express HENMT1 (17) vs lines expressing it (33) | 1.18× higher at baseline in the lines without HENMT1 | 0.082 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TOR1A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises TOR1A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-16.4, -27.7); signed map (23.5, -29.6). **Vector** length 89.9, 18.1% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +5.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +8.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +2.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.0 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -9.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | -11.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -4.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | torsin family 1 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,812,942-129,824,244 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DQ2; previously DYT1 |
| Gene groups (HGNC) | Torsins |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O14656](https://www.uniprot.org/uniprotkb/O14656) (Torsin-1A):

> Protein with chaperone functions important for the control of protein folding, processing, stability and localization as well as for the reduction of misfolded protein aggregates. Involved in the regulation of synaptic vesicle recycling, controls STON2 protein stability in collaboration with the COP9 signalosome complex (CSN). In the nucleus, may link the cytoskeleton with the nuclear envelope, this mechanism seems to be crucial for the control of nuclear polarity, cell movement and, …

**Summary**, from NCBI Gene [1861](https://www.ncbi.nlm.nih.gov/gene/1861):

> The protein encoded by this gene is a member of the AAA family of adenosine triphosphatases (ATPases), is related to the Clp protease/heat shock family and is expressed prominently in the substantia nigra pars compacta. Mutations in this gene result in the autosomal dominant disorder, torsion dystonia 1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3098) · Entrez [1861](https://www.ncbi.nlm.nih.gov/gene/1861) · UniProt [O14656](https://www.uniprot.org/uniprotkb/O14656) · Ensembl [ENSG00000136827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136827)

## Data

Gene col 5912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5912); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5912]; `tensor/DDL_lfc|DDL_z.npy` [5912]; `embed/gene_vectors.npy` [5912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5912 or target_col == 5912). Every well: [[TOR1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOR1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
