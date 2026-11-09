---
symbol: "POLR2K"
type: "gene"
col: 7212
ensembl_id: "ENSG00000147669"
name: "RNA polymerase II, I and III subunit K"
location: "8q22.2"
module: 48
arm: "+"
pooled_cpm: 25.6
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# POLR2K

*RNA polymerase II, I and III subunit K* — 8q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (20 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.37× (z +10.5, q 5e-23, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (H4 0.0715×; ⚠ cell-cycle shift, would explain all of this change); [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW48 0.0754×; ⚠ transcription drop; unreliable plate only).
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 32 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL51]] (+0.64, fdr 1e-05, ⚠ MRPL51 in the vector space only through flagged drug-doses), [[COPS9]] (+0.63, fdr 1e-05), [[ATP5MF]] (+0.61, fdr 9e-06), [[UBL5]] (+0.60, fdr 2e-04); moves opposite to [[CCDC6]] (-0.54, fdr 3e-05), [[AZIN1]] (-0.54, fdr 3e-05), [[EEF2]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 20 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +10.5 | 5e-23 | 44/47 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **3.20×** | +10.2 | 4e-22 | 39/42 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.87×** | +9.3 | 3e-18 | 47/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.84×** | +9.2 | 6e-18 | 48/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.57×** | +8.3 | 1e-14 | 46/47 (LoVo, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.66×** | +8.3 | 1e-14 | 43/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **2.54×** | +7.9 | 2e-13 | 27/33 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.35×** | +7.5 | 4e-12 | 44/46 (PANC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **2.21×** | +6.5 | 6e-09 | 33/37 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **2.03×** | +6.0 | 1e-07 | 33/47 (NCI-H1573, HOP62, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.95×** | +5.9 | 2e-07 | 39/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.92×** | +5.5 | 2e-06 | 33/47 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.88×** | +5.4 | 4e-06 | 31/48 (SW480, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +5.3 | 5e-06 | 29/47 (NCI-H1573, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.2 | 7e-06 | 32/48 (HOP62, A-172, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.011 | 23/47 (A498, A-172, …) | top dose only | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.89×** | +3.1 | 0.047 | 22/47 (HOP62, H4, …) | rises with dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.051 | 18/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.88×** | +2.9 | 0.077 | 15/44 (PANC-1, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7212.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (H4 0.0715×; ⚠ cell-cycle shift, would explain all of this change); [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW48 0.0754×; ⚠ transcription drop; unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.462× | -3.5 | 0.24 | 28/46 (A498, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.504× | -3.1 | 0.47 | 21/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.80 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 15.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +9.9) | — |
| [[SW480 (line)]] | alt | 21.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 16.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[A-172 (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.72× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[BT-474 (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.82× (z +8.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +9.7) | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0715× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 42.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 36.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[SW 900 (line)]] | alt | 31.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +8.6) | — |
| [[SW48 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0754× (z -9.3) ⚠ transcription drop; unreliable plate only |
| [[A-427 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 30 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL51]] ⚠ | +0.64 | +0.51 / +0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COPS9]] | +0.63 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[ATP5MF]] | +0.61 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[NDUFA13]] ⚠ | +0.60 | +0.60 / +0.62 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[UBL5]] | +0.60 | +0.30 / +0.64 | both halves | 2e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[POLR2L]] | +0.59 | +0.63 / +0.60 | both halves | 7e-06 | same gene group; pathway: Abortive elongation of HIV-1 transcript in the absence of Tat; STRING 999 |
| [[COX17]] | +0.59 | +0.54 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[GTF2A2]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_DNA_REPAIR; STRING 968 |
| [[ROMO1]] | +0.58 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[ATP5PF]] | +0.58 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[NDUFB1]] | +0.57 | +0.37 / +0.70 | both halves | 8e-05 |  |
| [[UQCRQ]] ⚠ | +0.56 | +0.32 / +0.64 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | +0.55 | +0.32 / +0.59 | both halves | 2e-04 |  |
| [[NDUFB3]] | +0.54 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[HSBP1]] | +0.53 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC6]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[AZIN1]] | -0.54 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[EEF2]] | -0.50 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[NPM1]] | -0.47 | -0.28 / -0.42 | both halves | 3e-04 | pathway: Chromosome Maintenance |
| [[LARS1]] | -0.47 | -0.15 / -0.50 | ⚠ not reproduced | 0.001 |  |
| [[EIF4B]] | -0.46 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[BACE1-AS]] | -0.46 | -0.15 / -0.48 | ⚠ not reproduced | 0.001 |  |
| [[LARP1]] | -0.46 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[PCBP2]] | -0.45 | -0.34 / -0.42 | both halves | 1e-04 | pathway: Dengue Virus-Host Interactions |
| [[NONO]] | -0.45 | -0.24 / -0.57 | both halves | 5e-04 |  |
| [[SSRP1]] | -0.45 | -0.35 / -0.39 | both halves | 1e-04 | pathway: HALLMARK_DNA_REPAIR; STRING 898 |
| [[EIF3C]] | -0.44 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[EPRS1]] | -0.44 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[TCEA1]] | -0.44 | -0.53 / -0.41 | both halves | 4e-05 | pathway: Affinity selection of immunoglobulins; STRING 990 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POLR2K's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.8, -21.8); signed map (-36.4, 9.8). **Vector** length 48.3, 10.3% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Complex I biogenesis* (reactome, mean cos +0.51 to 9); *Mitochondrial protein degradation* (reactome, mean cos +0.50 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +2.9 | +7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +2.5 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +10.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +2.3 | +5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | +0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~68% of this change | -1.8 | +4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | +0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II, I and III subunit K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.2 — chr8:100,150,623-100,154,003 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPB10alpha, RPB12 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 94 pathways, smallest: RNA Polymerase III Chain Elongation; Signaling by FGFR2 IIIa TM; PIWI-interacting RNA (piRNA) biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P53803](https://www.uniprot.org/uniprotkb/P53803) (DNA-directed RNA polymerases I, II, and III subunit RPABC4):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Common component of RNA polymerases I, II and III which synthesize ribosomal RNA precursors, mRNA precursors and many functional non-coding RNAs, and a small RNAs, such as 5S rRNA and tRNAs, respectively.

**Summary**, from NCBI Gene [5440](https://www.ncbi.nlm.nih.gov/gene/5440):

> This gene encodes one of the smallest subunits of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. This subunit is shared by the other two DNA-directed RNA polymerases. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9198](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9198) · Entrez [5440](https://www.ncbi.nlm.nih.gov/gene/5440) · UniProt [P53803](https://www.uniprot.org/uniprotkb/P53803) · Ensembl [ENSG00000147669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147669)

## Data

Gene col 7212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7212); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7212]; `tensor/DDL_lfc|DDL_z.npy` [7212]; `embed/gene_vectors.npy` [7212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7212 or target_col == 7212). Every well: [[POLR2K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
