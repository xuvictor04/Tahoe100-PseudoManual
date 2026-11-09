---
symbol: "FNDC7"
type: "gene"
col: 6678
ensembl_id: "ENSG00000143107"
name: "fibronectin type III domain containing 7"
location: "1p13.3"
module: 38
arm: "+"
pooled_cpm: 3.18
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/038", "written"]
generated_by: "tahoemap"
---

# FNDC7

*fibronectin type III domain containing 7* — 1p13.3

> [!summary] In one line
> FNDC7 encodes a predicted secreted protein built from fibronectin type III repeats, and essentially nothing about its function is established.

## What it is

What is known is sequence and little else. The open reading frame predicts a signal peptide and a string of fibronectin type III domains — a module shared with fibronectin itself and many cell-surface proteins, and the only basis for any family assignment. Expression is low wherever surveyed, most consistently in testis. Everything functional is annotation, not observation: "secreted" and "extracellular region" come from domain content, not experiment. There is no published knockout, no identified ligand or receptor, no characterised partner, no replicated disease association. No connection has been reported between FNDC7 and p53 or membrane repair.

## What is uncertain

Everything. The transcript is near the detection floor, and a testis-biased gene reading as weakly present across a pooled cancer-line panel is as easily explained by ambient RNA or by reads shared with other FN3-domain paralogues as by real expression. With no established function there is no prediction to test and no mechanism against which a correlation could be judged. Nothing here separates a real association from one driven by a few lines or by depth and ambient-RNA covariates.

## References

No primary literature I can cite with confidence.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.97× (z +18.0, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[HI-TOPK-032 (drug)]] 0.05 µM: 0.445× (z -4.5, q 0.004, down in 14 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0386×; ⚠ cell-cycle shift, explains ~25% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM72]] (+0.94, fdr 7e-06), [[MYOCOS]] (+0.89, fdr 7e-06), [[ARL9]] (+0.88, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.97×** | +18.0 | 0e+00 | 32/32 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **6.04×** | +14.7 | 0e+00 | 31/34 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **6.10×** | +10.1 | 1e-21 | 13/15 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **5.60×** | +10.0 | 3e-21 | 34/38 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.54×** | +8.7 | 2e-16 | 22/30 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.43×** | +8.0 | 2e-13 | 3/4 (A498, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.88×** | +7.5 | 4e-12 | 24/35 (RKO, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **3.52×** | +7.0 | 2e-10 | 1/3 (A498) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.26×** | +6.6 | 2e-09 | 16/42 (PANC-1, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +6.5 | 4e-09 | 15/28 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.55×** | +5.4 | 3e-06 | 25/45 (A498, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.48×** | +5.0 | 2e-05 | 23/38 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.28×** | +4.5 | 3e-04 | 16/38 (A498, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.91×** | +3.7 | 0.008 | 3/16 (LoVo, HOP62, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.90×** | +3.7 | 0.009 | 12/44 (A498, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.89×** | +3.7 | 0.009 | 5/39 (AsPC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.95×** | +3.3 | 0.032 | 2/17 (NCI-H460, NCI-H2030) | top dose only | noisy plate (z scaled); position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.035 | 9/41 (MIA PaCa-2, LOX-IMVI, …) | top dose only | position effect removed |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.063 | 8/42 (LoVo, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6678.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0386×; ⚠ cell-cycle shift, explains ~25% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.445×** | -4.5 | 0.004 | 14/35 (A498, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.654× | -3.6 | 0.11 | 12/44 (SK-MEL-2, SW 900, …) | all doses, flat | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.545× | -3.1 | 0.36 | 10/43 (MIA PaCa-2, H4, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.82 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 5.83 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +8.5) | [[Harringtonine (drug)]] 0.5 µM 0.0386× (z -9.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 2.67 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +11.4) | — |
| [[SW480 (line)]] | alt | 2.07 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.45× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 7.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 1.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.0× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 7.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +9.0) | — |
| [[A-172 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.885 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM72]] | +0.94 | +0.93 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[MYOCOS]] | +0.89 | +0.90 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[ARL9]] | +0.88 | +0.88 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[LDHC]] | +0.88 | +0.87 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[SELPLG]] | +0.88 | +0.88 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[IMPA1P1]] | +0.87 | +0.87 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[PYGM]] | +0.85 | +0.86 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[PILRA]] | +0.85 | +0.84 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[USP50]] | +0.85 | +0.86 / +0.80 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.85 | +0.83 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[ALDH8A1]] | +0.84 | +0.87 / +0.76 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.84 | +0.84 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FNDC7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYOM1]] | B | MYOM1 activity raises FNDC7's level | lines that do not express MYOM1 (9) vs lines expressing it (41) | 1.48× lower at baseline in the lines without MYOM1 | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC00334]] | B | LINC00334 activity raises FNDC7's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.85× lower at baseline in the lines without LINC00334 | 0.069 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[F2]] | B | F2 activity raises FNDC7's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.70× lower at baseline in the lines without F2 | 0.072 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC01291]] | B | LINC01291 activity raises FNDC7's level | lines that do not express LINC01291 (10) vs lines expressing it (40) | 1.48× lower at baseline in the lines without LINC01291 | 0.088 | ⚠ within organs, on part of the lines; also absent: ANTXR2, ENSG00000230479, PROCR; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.877). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.2, -15.7); signed map (16.6, 10.7). **Vector** length 88.4, 19.4% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +18.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +14.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +5.5 | +7.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.8 | +4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.3 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +6.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +3.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +1.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.9 | -4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -2.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | fibronectin type III domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:108,712,908-108,742,749 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35838 |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Matched by | ensembl_id |

UniProt [Q5VTL7](https://www.uniprot.org/uniprotkb/Q5VTL7) carries no function annotation.

**Summary**, from NCBI Gene [163479](https://www.ncbi.nlm.nih.gov/gene/163479):

> Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26668) · Entrez [163479](https://www.ncbi.nlm.nih.gov/gene/163479) · UniProt [Q5VTL7](https://www.uniprot.org/uniprotkb/Q5VTL7) · Ensembl [ENSG00000143107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143107)

## Data

Gene col 6678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6678); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6678]; `tensor/DDL_lfc|DDL_z.npy` [6678]; `embed/gene_vectors.npy` [6678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6678 or target_col == 6678). Every well: [[FNDC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/FNDC7.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
