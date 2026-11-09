---
symbol: "DMWD"
type: "gene"
col: 11733
ensembl_id: "ENSG00000185800"
name: "DM1 locus, WD repeat containing"
location: "19q13.32"
module: 138
arm: "+"
pooled_cpm: 13.56
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# DMWD

*DM1 locus, WD repeat containing* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.75× (z +12.8, q 8e-35, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.770× (z -4.2, q 0.012, down in 13 of 47 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.783× (z -4.0, q 0.013, down in 16 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (drug)]] 0.05 µM in 1 line (BT-474 0.0723×); [[Selinexor (drug)]] 5 µM in 1 line (MIA PaCa-2 0.311×; ⚠ cell-cycle shift, explains ~1% of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0970×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACTIN]] (+0.73, fdr 7e-06), [[FBRS]] (+0.69, fdr 7e-06), [[TAOK2]] (+0.65, fdr 1e-05); moves opposite to [[ATG4C]] (-0.55, fdr 2e-05), [[HIBADH]] (-0.52, fdr 4e-05), [[ABHD10]] (-0.51, fdr 3e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11733.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +12.8 | 8e-35 | 33/47 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +10.1 | 2e-21 | 17/23 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +9.9 | 7e-21 | 28/35 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +8.9 | 1e-16 | 31/45 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +8.2 | 3e-14 | 28/45 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +7.8 | 6e-13 | 28/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.6 | 4e-09 | 27/46 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +6.1 | 9e-08 | 27/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.5 | 3e-06 | 20/48 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 1e-05 | 17/46 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.36×** | +4.9 | 4e-05 | 15/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +4.9 | 4e-05 | 20/46 (HOP62, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +4.8 | 7e-05 | 19/46 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.37×** | +4.7 | 9e-05 | 16/31 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +4.6 | 1e-04 | 16/47 (HEC-1-A, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 3e-04 | 15/44 (hTERT-HPNE, HCT15, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.009 | 6/45 (HEC-1-A, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Regorafenib (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.014 | 5/48 (HS-578T, SHP-77, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.049 | 8/43 (J82, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Berbamine (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.061 | 7/48 (LOX-IMVI, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11733.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (drug)]] 0.05 µM in 1 line (BT-474 0.0723×); [[Selinexor (drug)]] 5 µM in 1 line (MIA PaCa-2 0.311×; ⚠ cell-cycle shift, explains ~1% of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0970×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.770×** | -4.2 | 0.012 | 13/47 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.839× | -4.1 | 0.013 | 17/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.783×** | -4.0 | 0.013 | 16/46 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | **0.800×** | -3.6 | 0.040 | 9/48 (HEC-1-A, HT-29, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.858× | -3.5 | 0.045 | 19/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.875× | -3.1 | 0.17 | 6/48 (NCI-H2030, SW48, …) | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 0.05 µM |  | 0.816× | -3.1 | 0.17 | 4/46 (SW48, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 9.84 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0723× (z -12.0) |
| [[COLO 205 (line)]] | alt | 8.19 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0990× (z -8.9) ⚠ toxic; unreliable plate only |
| [[HOP62 (line)]] | alt | 45.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.311× (z -10.1) ⚠ cell-cycle shift, explains ~1% of this change |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0970× (z -9.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +8.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 9.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.5) | — |
| [[A-172 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACTIN]] | +0.73 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[FBRS]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[TAOK2]] | +0.65 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[CEP170B]] | +0.64 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[AGRN]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[BRD9]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[WIZ]] | +0.63 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[KDM6B]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[CYTH2]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[RGL2]] | +0.61 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[ATN1]] | +0.61 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[RHBDF1]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4C]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[HIBADH]] | -0.52 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ABHD10]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[LDHB]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CDC40]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 | same gene group |
| [[DNAJC19]] | -0.50 | -0.59 / -0.32 | both halves | 1e-04 |  |
| [[PET117]] | -0.50 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[CBR1]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DMWD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.770). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.5, -22.7); signed map (2.2, -7.8). **Vector** length 65.9, 9.87% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.0 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +4.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +0.8 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.4 | +3.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.2 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -2.4 | -4.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | DM1 locus, WD repeat containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,782,947-45,792,845 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DMR-N9, gene59, D19S593E |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q09019](https://www.uniprot.org/uniprotkb/Q09019) (Dystrophia myotonica WD repeat-containing protein):

> Regulator of the deubiquitinating USP12/DMWD/WDR48 complex. Functions as a cofactor that promotes USP12 enzymatic activity.

**Summary**, from NCBI Gene [1762](https://www.ncbi.nlm.nih.gov/gene/1762):

> Enables deubiquitinase activator activity. Predicted to be involved in negative regulation of ubiquitin-dependent protein catabolic process. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:2936](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2936) · Entrez [1762](https://www.ncbi.nlm.nih.gov/gene/1762) · UniProt [Q09019](https://www.uniprot.org/uniprotkb/Q09019) · Ensembl [ENSG00000185800](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185800)

## Data

Gene col 11733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11733); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11733]; `tensor/DDL_lfc|DDL_z.npy` [11733]; `embed/gene_vectors.npy` [11733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11733 or target_col == 11733). Every well: [[DMWD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMWD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
