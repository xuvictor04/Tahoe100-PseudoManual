---
symbol: "ABCA6"
type: "gene"
col: 7790
ensembl_id: "ENSG00000154262"
name: "ATP binding cassette subfamily A member 6"
location: "17q24.2-q24.3"
module: 10
arm: "+"
pooled_cpm: 2.36
n_lines_expressing: 24
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 7
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ABCA6

*ATP binding cassette subfamily A member 6* — 17q24.2-q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 21.1× (z +24.6, q 0e+00, up in 12 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0200×; ⚠ cell-cycle shift, explains ~41% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0306×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.142×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TG]] (+0.69, fdr 3e-05), [[ANGPT2]] (+0.65, fdr 4e-05), [[LINC00240]] (+0.64, fdr 3e-05); moves opposite to [[RALGPS1]] (-0.61, fdr 4e-05), [[ATP7B]] (-0.58, fdr 6e-05), [[FAM20B]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[ABCA10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7790.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **21.1×** | +24.6 | 0e+00 | 12/13 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.09×** | +14.5 | 3e-45 | 7/10 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.03×** | +10.2 | 3e-22 | 2/4 (MIA PaCa-2, C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.00×** | +10.2 | 3e-22 | 8/11 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.47×** | +9.3 | 2e-18 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.92×** | +7.1 | 9e-11 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **2.13×** | +6.0 | 1e-07 | 3/17 (SNU-1, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.91×** | +5.8 | 4e-07 | 2/7 (NCI-H460, SW 900) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +5.0 | 4e-05 | 4/17 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.46×** | +4.9 | 5e-05 | 8/17 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.33×** | +4.8 | 8e-05 | 4/11 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +4.7 | 1e-04 | 3/11 (NCI-H460, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +4.2 | 0.001 | 1/19 (hTERT-HPNE) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.24×** | +4.1 | 0.002 | 7/12 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.5 | 0.017 | 1/7 (HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.83×** | +3.4 | 0.024 | 6/18 (HS-578T, NCI-H1792, …) | all doses, flat |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.82×** | +3.4 | 0.025 | 1/9 (CFPAC-1) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.81×** | +3.4 | 0.025 | 8/13 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.48×** | +3.1 | 0.052 | 4/16 (NCI-H1792, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0200×; ⚠ cell-cycle shift, explains ~41% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.0306×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.142×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 65.4 | 0 | 7 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0200× (z -15.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 1.68 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 69.6× (z +15.8) | — |
| [[C32 (line)]] | wt | 6.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 2.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 3.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.3× (z +8.6) | — |
| [[A-172 (line)]] | wt | 0.247 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.199 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.634 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.751 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.687 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.849 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.649 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.677 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.176 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.733 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.280 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 10 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TG]] | +0.69 | +0.72 / +0.46 | both halves | 3e-05 |  |
| [[ANGPT2]] | +0.65 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[LINC00240]] | +0.64 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[IPCEF1]] | +0.63 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[AGA-DT]] | +0.60 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[RP1]] | +0.60 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[SAMSN1]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[TMEM202-AS1]] | +0.58 | +0.62 / +0.27 | both halves | 3e-04 |  |
| [[SVEP1]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[DPY19L2P2]] | +0.58 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[NEB]] | +0.58 | +0.61 / +0.27 | both halves | 3e-04 |  |
| [[PCNX4-DT]] | +0.58 | +0.62 / +0.29 | both halves | 3e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALGPS1]] | -0.61 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[ATP7B]] | -0.58 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[FAM20B]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[FAM118A]] | -0.53 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[UBA6]] | -0.52 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[PPM1F]] | -0.52 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[TBC1D24]] | -0.52 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[COPG2]] | -0.52 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[ANKRD27]] | -0.51 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[GNA12]] | -0.51 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[COG5]] | -0.51 | -0.51 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ABCA6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA10]] | B | ABCA6 activity raises ABCA10's level | lines that do not express ABCA6 (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without ABCA6 | 2e-04 | ⚠ within organs, on part of the lines; also absent: LINC02154, IGF2, LYPLAL1-DT |
| [[ITGA10]] | B | ABCA6 activity raises ITGA10's level | lines that do not express ABCA6 (26) vs lines expressing it (24) | 2.44× lower at baseline in the lines without ABCA6 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC02154, IGF2, LYPLAL1-DT |
| [[LINC01252]] | B | ABCA6 activity raises LINC01252's level | lines that do not express ABCA6 (26) vs lines expressing it (24) | 1.57× lower at baseline in the lines without ABCA6 | 0.065 | ⚠ within organs, on part of the lines; also absent: LINC02154, IGF2, LYPLAL1-DT |
| [[DPH6-DT]] | B | ABCA6 activity raises DPH6-DT's level | lines that do not express ABCA6 (26) vs lines expressing it (24) | 1.49× lower at baseline in the lines without ABCA6 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC02154, IGF2, LYPLAL1-DT |
| [[LINC00607]] | B | ABCA6 activity raises LINC00607's level | lines that do not express ABCA6 (26) vs lines expressing it (24) | 1.51× lower at baseline in the lines without ABCA6 | 0.083 | ⚠ within organs, on part of the lines; also absent: LINC02154, IGF2, LYPLAL1-DT |
| [[ITGA9]] | B | ABCA6 activity raises ITGA9's level | lines that do not express ABCA6 (26) vs lines expressing it (24) | 1.47× lower at baseline in the lines without ABCA6 | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC02154, IGF2, LYPLAL1-DT |
| [[GYPC]] | C | ABCA6 activity raises GYPC's level | lines that do not express ABCA6 (26) vs lines expressing it (24) | 2.29× lower at baseline in the lines without ABCA6 | 0.061 | ⚠ within organs, on part of the lines; also absent: LINC02154, IGF2, LYPLAL1-DT; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (24.6, 21.5); signed map (26.4, 12.7). **Vector** length 39.3, 9.67% of its response variance represented; |z| ≥ 3 in 389 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +24.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +10.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +14.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +4.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.1 | +3.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.1 | +2.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -1.5 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | -1.1 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.1 | -0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily A member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2-q24.3 — chr17:69,078,702-69,141,895 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EST155051 |
| Gene groups (HGNC) | ATP binding cassette subfamily A; MicroRNA protein coding host genes |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 5 pathways, smallest: ABC transporters in lipid homeostasis; FOXO-mediated transcription of oxidative stress, metabolic and neuronal genes; FOXO-mediated transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N139](https://www.uniprot.org/uniprotkb/Q8N139) (ATP-binding cassette sub-family A member 6):

> Probable transporter which may play a role in macrophage lipid transport and homeostasis.

**Summary**, from NCBI Gene [23460](https://www.ncbi.nlm.nih.gov/gene/23460):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intracellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, and White). This encoded protein is a member of the ABC1 subfamily. Members of the ABC1 subfamily comprise the only major ABC subfamily found exclusively in multicellular eukaryotes. This gene …

**Accessions** — [HGNC:36](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:36) · Entrez [23460](https://www.ncbi.nlm.nih.gov/gene/23460) · UniProt [Q8N139](https://www.uniprot.org/uniprotkb/Q8N139) · Ensembl [ENSG00000154262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154262)

## Data

Gene col 7790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7790); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7790]; `tensor/DDL_lfc|DDL_z.npy` [7790]; `embed/gene_vectors.npy` [7790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7790 or target_col == 7790). Every well: [[ABCA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
