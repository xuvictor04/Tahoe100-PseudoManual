---
symbol: "HIC2"
type: "gene"
col: 9830
ensembl_id: "ENSG00000169635"
name: "HIC ZBTB transcriptional repressor 2"
location: "22q11.21"
module: 25
arm: "-"
pooled_cpm: 16.54
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# HIC2

*HIC ZBTB transcriptional repressor 2* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +9.0, q 1e-16, up in 40 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.0751×; ⚠ cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 900 0.0764×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.232×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PI4KAP2]] (+0.67, fdr 1e-05, ⚠ same locus), [[PI4KAP1]] (+0.64, fdr 1e-05), [[TNRC6C]] (+0.62, fdr 9e-06), [[RBM38]] (+0.62, fdr 1e-05); moves opposite to [[RBBP9]] (-0.69, fdr 7e-06), [[DLD]] (-0.66, fdr 7e-06), [[ATIC]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PI4KAP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +9.0 | 1e-16 | 40/45 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +7.8 | 2e-12 | 34/44 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.95×** | +7.2 | 1e-10 | 38/46 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.74×** | +6.0 | 3e-07 | 35/48 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +5.2 | 2e-05 | 31/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.58×** | +4.9 | 7e-05 | 32/48 (Panc 03.27, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.57×** | +4.9 | 9e-05 | 28/48 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.7 | 1e-04 | 26/46 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.45×** | +4.0 | 0.004 | 25/48 (AsPC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.44×** | +3.9 | 0.004 | 18/40 (LoVo, SHP-77, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.45×** | +3.9 | 0.006 | 14/30 (LoVo, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.38×** | +3.5 | 0.021 | 16/48 (LoVo, SW480, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.054 | 18/47 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.10 | 15/47 (hTERT-HPNE, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9830.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.0751×; ⚠ cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 900 0.0764×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.232×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.698× | -3.6 | 0.21 | 13/47 (NCI-H460, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.736× | -3.0 | 0.70 | 13/47 (hTERT-HPNE, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 25.0 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.51× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 13.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +16.7) | — |
| [[AsPC-1 (line)]] | alt | 19.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 20.3 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.64× (z +10.3) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0751× (z -13.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +8.7) | — |
| [[NCI-H661 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0653× (z -8.8) ⚠ transcription drop |
| [[PANC-1 (line)]] | alt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0764× (z -13.1) |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PI4KAP2]] | +0.67 | +0.56 / +0.69 | both halves | 1e-05 | ⚠ same locus (21.6 kb: neighbours can correlate without regulation) |
| [[PI4KAP1]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TNRC6C]] | +0.62 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[RBM38]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[RABGEF1]] | +0.62 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[EIF1B]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ZBTB7A]] | +0.61 | +0.57 / +0.65 | both halves | 1e-05 | same gene group |
| [[TOB2]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[FBXL12]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[CDC34]] | +0.59 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[RAB11FIP3]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[PHKG1]] | +0.58 | +0.48 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP9]] | -0.69 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[DLD]] | -0.66 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[ATIC]] | -0.65 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[IPO8]] | -0.65 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[ALG10]] | -0.64 | -0.41 / -0.72 | both halves | 4e-05 |  |
| [[PRELID3B]] | -0.63 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[DHX9]] | -0.63 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[UBQLN1]] | -0.63 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[ALG10B]] | -0.62 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[FH]] | -0.61 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[SLX4IP]] | -0.61 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[CCT7]] | -0.60 | -0.54 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PI4KAP1]] | B | PI4KAP1 activity raises HIC2's level | lines that do not express PI4KAP1 (24) vs lines expressing it (26) | 1.39× lower at baseline in the lines without PI4KAP1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1-1, ENSG00000260573, LCK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.2, -16.8); signed map (-32.7, 13.8). **Vector** length 83.9, 18.5% of its response variance represented; |z| ≥ 3 in 680 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.5 | +6.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.4 | +7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.4 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +9.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +7.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.7 | +1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | +0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.2 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | -2.6 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | HIC ZBTB transcriptional repressor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:21,417,371-21,451,463 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1020, HRG22, ZBTB30, ZNF907 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JB3](https://www.uniprot.org/uniprotkb/Q96JB3) (Hypermethylated in cancer 2 protein):

> Transcriptional repressor.

**Summary**, from NCBI Gene [23119](https://www.ncbi.nlm.nih.gov/gene/23119):

> Predicted to enable DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II; regulation of cytokine production; and regulation of immune system process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18595](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18595) · Entrez [23119](https://www.ncbi.nlm.nih.gov/gene/23119) · UniProt [Q96JB3](https://www.uniprot.org/uniprotkb/Q96JB3) · Ensembl [ENSG00000169635](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169635)

## Data

Gene col 9830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9830); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9830]; `tensor/DDL_lfc|DDL_z.npy` [9830]; `embed/gene_vectors.npy` [9830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9830 or target_col == 9830). Every well: [[HIC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
