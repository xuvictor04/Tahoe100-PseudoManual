---
symbol: "SYN3"
type: "gene"
col: 11714
ensembl_id: "ENSG00000185666"
name: "synapsin III"
location: "22q12.3"
module: 166
arm: "+"
pooled_cpm: 14.16
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# SYN3

*synapsin III* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.17× (z +14.4, q 2e-44, up in 25 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.26× (z +14.4, q 2e-44, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Balsalazide (sodium hydrate) (drug)]] 5 µM: 0.800× (z -3.9, q 0.054, down in 11 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (H4 0.0518×, RPMI-7951 0.112×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RPMI-7951 0.231×, Hs 766T 0.294×); [[Digitoxin (drug)]] 5 µM in 1 line (H4 0.0581×; ⚠ toxic; transcription drop); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0841×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SORCS1]] (+0.75, fdr 7e-06), [[ALK]] (+0.72, fdr 7e-06), [[CNTN5]] (+0.71, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TDRD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11714.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.17×** | +14.4 | 2e-44 | 25/34 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +14.4 | 2e-44 | 32/43 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +11.3 | 4e-27 | 11/17 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +10.7 | 1e-24 | 36/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +10.0 | 3e-21 | 26/45 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +8.9 | 4e-17 | 17/25 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +7.7 | 9e-13 | 28/48 (A549, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +6.2 | 4e-08 | 21/46 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +6.0 | 1e-07 | 23/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.5 | 2e-06 | 18/45 (BT-474, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.5 | 3e-04 | 18/46 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.1 | 0.002 | 14/43 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.5 | 0.019 | 16/46 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.025 | 19/48 (A549, C-33 A, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.025 | 11/47 (SW48, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.048 | 16/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.076 | 14/45 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11714.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (H4 0.0518×, RPMI-7951 0.112×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RPMI-7951 0.231×, Hs 766T 0.294×); [[Digitoxin (drug)]] 5 µM in 1 line (H4 0.0581×; ⚠ toxic; transcription drop); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0841×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | **0.800×** | -3.9 | 0.054 | 11/48 (LoVo, A-172, …) | inconsistent across doses | position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | 0.815× | -3.6 | 0.10 | 13/47 (A549, LoVo, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.761× | -3.3 | 0.17 | 11/48 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.774× | -3.2 | 0.22 | 10/48 (RPMI-7951, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM |  | 0.780× | -3.1 | 0.24 | 3/48 (C32, HepG2/C3A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11714. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 15.0 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 6.04× (z +11.7) | — |
| [[C32 (line)]] | wt | 80.1 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.57× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.179× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[NCI-H1573 (line)]] | alt | 42.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.28× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 6.09 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 6.84× (z +13.4) | — |
| [[RPMI-7951 (line)]] | alt | 63.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -10.8) |
| [[H4 (line)]] | wt | 28.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0518× (z -12.4) |
| [[C-33 A (line)]] | alt | 7.99 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.33× (z +9.9) | — |
| [[HCT15 (line)]] | alt | 6.78 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.0602× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 5.90 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.31× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 7.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 78.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.7) |
| [[KATO III (line)]] | alt | 6.65 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.7× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 5.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0902× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 4.77 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0841× (z -9.5) |
| [[A-172 (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 148 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11714), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORCS1]] | +0.75 | +0.64 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ALK]] | +0.72 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[CNTN5]] | +0.71 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[OBI1-AS1]] | +0.70 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[CNTN4]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[PKNOX2]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SNX32]] | +0.66 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[DLGAP2]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 | pathway: Neuronal System |
| [[LINC01500]] | +0.66 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[RETREG1-AS1]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[TIMP3]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 | STRING 555; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SLC14A2]] | +0.64 | +0.60 / +0.57 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TDRD9]] | B | TDRD9 activity raises SYN3's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 2.31× lower at baseline in the lines without TDRD9 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT |
| [[DIRC3]] | B | DIRC3 activity raises SYN3's level | lines that do not express DIRC3 (19) vs lines expressing it (31) | 2.07× lower at baseline in the lines without DIRC3 | 0.047 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[TIMP3]] | B | TIMP3 activity raises SYN3's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 2.18× lower at baseline in the lines without TIMP3 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[TOP2A]] | B | TOP2A activity lowers SYN3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.0, 32.4); signed map (29.7, 17.4). **Vector** length 81.6, 15.1% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.8 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.1 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.0 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.0 | -3.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.1 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.1 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | synapsin III |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:32,507,820-33,058,381 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Synapsins |
| Reactome | 5 pathways, smallest: Serotonin Neurotransmitter Release Cycle; Dopamine Neurotransmitter Release Cycle; Neurotransmitter release cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O14994](https://www.uniprot.org/uniprotkb/O14994) (Synapsin-3):

> May be involved in the regulation of neurotransmitter release and synaptogenesis.

**Summary**, from NCBI Gene [8224](https://www.ncbi.nlm.nih.gov/gene/8224):

> This gene is a member of the synapsin gene family. Synapsins encode neuronal phosphoproteins which associate with the cytoplasmic surface of synaptic vesicles. Family members are characterized by common protein domains, and they are implicated in synaptogenesis and the modulation of neurotransmitter release, suggesting a potential role in several neuropsychiatric diseases. The protein encoded by this gene shares the synapsin family domain model, with domains A, C, and E exhibiting the highest …

**Accessions** — [HGNC:11496](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11496) · Entrez [8224](https://www.ncbi.nlm.nih.gov/gene/8224) · UniProt [O14994](https://www.uniprot.org/uniprotkb/O14994) · Ensembl [ENSG00000185666](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185666)

## Data

Gene col 11714: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11714); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11714, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11714]; `tensor/DDL_lfc|DDL_z.npy` [11714]; `embed/gene_vectors.npy` [11714]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11714 or target_col == 11714). Every well: [[SYN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
