---
symbol: "PIDD1"
type: "gene"
col: 10837
ensembl_id: "ENSG00000177595"
name: "p53-induced death domain protein 1"
location: "11p15.5"
module: 62
arm: "+"
pooled_cpm: 3.74
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# PIDD1

*p53-induced death domain protein 1* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.74× (z +9.9, q 2e-20, up in 3 of 5 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.79× (z +8.4, q 8e-15, up in 25 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.574× (z -5.7, q 6e-06, down in 16 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Asciminib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0683×); [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM in 1 line (C-33 A 0.0708×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FDXR]] (+0.72, fdr 7e-06), [[MAMDC4]] (+0.65, fdr 1e-05), [[MIB2]] (+0.64, fdr 1e-05); moves opposite to [[CBX3]] (-0.48, fdr 4e-05), [[LRBA]] (-0.46, fdr 1e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.74×** | +9.9 | 2e-20 | 3/5 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.31×** | +8.5 | 4e-15 | 11/16 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +8.4 | 8e-15 | 25/37 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +7.4 | 2e-11 | 17/37 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **2.06×** | +7.1 | 1e-10 | 11/21 (LS 180, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.88×** | +6.5 | 1e-08 | 19/45 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.87×** | +6.1 | 7e-08 | 15/31 (A498, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.2 | 2e-05 | 10/44 (RKO, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +5.1 | 2e-05 | 6/19 (A-172, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.9 | 6e-05 | 13/45 (A498, A549, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.85×** | +4.5 | 3e-04 | 6/28 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.49×** | +3.9 | 0.005 | 11/39 (A498, A549, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.69×** | +3.8 | 0.006 | 2/6 (PANC-1, SW480) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.45×** | +3.7 | 0.010 | 11/43 (LS 180, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.010 | 7/45 (A-427, RKO, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +3.6 | 0.010 | 8/26 (LS 180, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.019 | 11/43 (A549, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.022 | 3/33 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.57×** | +3.3 | 0.032 | 4/41 (A498, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.069 | 3/27 (SW480, SW1417, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.51×** | +3.0 | 0.072 | 3/31 (SHP-77, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10837.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Asciminib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0683×); [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM in 1 line (C-33 A 0.0708×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.574×** | -5.7 | 6e-06 | 16/43 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Allantoin (drug)]] 0.5 µM |  | 0.724× | -3.3 | 0.19 | 9/40 (RPMI-7951, KATO III, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | 0.727× | -3.3 | 0.19 | 8/37 (NCI-H2030, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.734× | -3.2 | 0.20 | 11/41 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.35 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.28× (z +8.7) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[C-33 A (line)]] | alt | 6.58 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM 0.0708× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 2.04 | 0 | 1 | — | [[Asciminib (drug)]] 0.05 µM 0.0683× (z -8.8) |
| [[A-172 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDXR]] | +0.72 | +0.62 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[MAMDC4]] | +0.65 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[MIB2]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[DDB2]] | +0.63 | +0.49 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 435 |
| [[RABGGTA]] | +0.62 | +0.38 / +0.62 | both halves | 6e-05 | pathway: TP53 Regulates Transcription of Cell Death Genes |
| [[GRIN2C]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[INKA2]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[BAX]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[TYMSOS]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SPATA18]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[PCED1A]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[MDM2]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 526 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX3]] | -0.48 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[LRBA]] | -0.46 | -0.47 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIDD1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.656). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.2, -26.2); signed map (40.1, -24.2). **Vector** length 51.4, 6.89% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *apoptosis* (hallmark, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.2 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.9 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +3.5 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +3.1 | +7.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -0.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +1.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Adenosine (drug)]] 0.5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | p53-induced death domain protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:799,179-809,753 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC16925, DKFZp434D229; previously LRDD, PIDD |
| Gene groups (HGNC) | ZU5 domain containing ; Caspase-2 PIDDosome complex |
| Hallmark sets | P53_PATHWAY |
| Reactome | 3 pathways, smallest: TP53 Regulates Transcription of Caspase Activators and Caspases; TP53 Regulates Transcription of Cell Death Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

UniProt [C0HMD6](https://www.uniprot.org/uniprotkb/C0HMD6) carries no function annotation.

**Summary**, from NCBI Gene [55367](https://www.ncbi.nlm.nih.gov/gene/55367):

> The protein encoded by this gene contains a leucine-rich repeat and a death domain. This protein has been shown to interact with other death domain proteins, such as Fas (TNFRSF6)-associated via death domain (FADD) and MAP-kinase activating death domain-containing protein (MADD), and thus may function as an adaptor protein in cell death-related signaling processes. The expression of the mouse counterpart of this gene has been found to be positively regulated by the tumor suppressor p53 and to …

**Accessions** — [HGNC:16491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16491) · Entrez [55367](https://www.ncbi.nlm.nih.gov/gene/55367) · UniProt [C0HMD6](https://www.uniprot.org/uniprotkb/C0HMD6) · Ensembl [ENSG00000177595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177595)

## Data

Gene col 10837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10837); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10837]; `tensor/DDL_lfc|DDL_z.npy` [10837]; `embed/gene_vectors.npy` [10837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10837 or target_col == 10837). Every well: [[PIDD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIDD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
