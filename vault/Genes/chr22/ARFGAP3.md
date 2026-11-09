---
symbol: "ARFGAP3"
type: "gene"
col: 14308
ensembl_id: "ENSG00000242247"
name: "ARF GTPase activating protein 3"
location: "22q13.2"
module: 56
arm: "+"
pooled_cpm: 147.0
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# ARFGAP3

*ARF GTPase activating protein 3* — 22q13.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 4.45×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 2.16×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 2.02×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.669× (z -11.4, q 3e-27, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WIPI1]] (+0.73, fdr 7e-06), [[HM13]] (+0.73, fdr 7e-06), [[SELENOS]] (+0.72, fdr 7e-06); moves opposite to [[MTMR2]] (-0.63, fdr 2e-05), [[SF3B4]] (-0.61, fdr 1e-05), [[ZNF507]] (-0.61, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GK]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SK-MEL-2 4.45×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 2.16×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 2.02×).

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14308.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.669×** | -11.4 | 3e-27 | 36/48 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.359×** | -10.7 | 2e-24 | 47/49 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.715×** | -9.5 | 4e-19 | 39/48 (RPMI-7951, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -8.3 | 1e-14 | 33/49 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.462×** | -8.1 | 6e-14 | 38/48 (Panc 03.27, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.832×** | -5.2 | 2e-05 | 24/48 (HOP62, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.783×** | -4.6 | 3e-04 | 30/47 (hTERT-HPNE, SW48, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.791×** | -4.5 | 5e-04 | 25/47 (hTERT-HPNE, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.803×** | -4.4 | 8e-04 | 25/48 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.791×** | -4.3 | 8e-04 | 25/45 (A498, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | **0.799×** | -4.3 | 9e-04 | 22/44 (HEC-1-A, LoVo, …) | all doses, flat | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.825×** | -3.8 | 0.006 | 26/48 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.825×** | -3.7 | 0.010 | 21/48 (LoVo, NCI-H661, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.711×** | -3.6 | 0.015 | 19/38 (NCI-H1573, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.838× | -3.5 | 0.017 | 22/48 (A549, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.832×** | -3.4 | 0.020 | 20/47 (HS-578T, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.886× | -3.4 | 0.020 | 14/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.853× | -3.2 | 0.042 | 11/48 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.859× | -3.0 | 0.065 | 16/48 (LS 180, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 139 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -13.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.178× (z -11.3) |
| [[A498 (line)]] | wt | 237 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -12.9) |
| [[HOP62 (line)]] | alt | 213 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 134 | 0 | 4 | — | [[TAK-901 (drug)]] 5 µM 0.202× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 275 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 178 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -17.9) |
| [[AsPC-1 (line)]] | alt | 204 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -13.0) |
| [[Hs 766T (line)]] | wt | 221 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.617× (z -9.0) |
| [[LoVo (line)]] | wt | 177 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.209× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 182 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -17.7) |
| [[RPMI-7951 (line)]] | alt | 174 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.544× (z -10.9) |
| [[SW 900 (line)]] | alt | 169 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.578× (z -9.9) |
| [[A-427 (line)]] | wt | 73.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -13.8) |
| [[A549 (line)]] | wt | 116 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -15.8) |
| [[H4 (line)]] | wt | 174 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.520× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 117 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.449× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.313× (z -8.6) |
| [[KATO III (line)]] | alt | 207 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.558× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 167 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.381× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 95.2 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.155× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 86.5 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.45× (z +14.8) | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -11.9) |
| [[AN3 CA (line)]] | alt | 116 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0628× (z -9.8) |
| [[BT-474 (line)]] | alt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -9.8) |
| [[COLO 205 (line)]] | alt | 169 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 394 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -8.5) |
| [[HT-29 (line)]] | alt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 61.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -10.7) |
| [[SNU-1 (line)]] | wt | 122 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.142× (z -9.6) |
| [[SNU-423 (line)]] | alt | 253 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.7) |
| [[A-172 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 215 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 175 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 117 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WIPI1]] | +0.73 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[HM13]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[SELENOS]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[SLC17A5]] | +0.71 | +0.65 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDXDC2P-NPIPB14P]] | +0.69 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[PGM3]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[GOLGA2]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC61B]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 635 |
| [[ACBD3]] | +0.67 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[TMEM263]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[MYDGF]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR2]] | -0.63 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[SF3B4]] | -0.61 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ANKRD40]] | -0.60 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[TGFBRAP1]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[FAM98B]] | -0.57 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[ZNF300]] | -0.57 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SF3B3]] | -0.57 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[BTBD1]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[SETD4]] | -0.56 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[DARS2]] | -0.56 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[UTP15]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GK]] | C | GK activity raises ARFGAP3's level | lines that do not express GK (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without GK | 0.050 | ⚠ few lines (4 vs 46); across organs; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.3, -35.4); signed map (-48.8, 12.3). **Vector** length 142, 47.0% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *COPII-mediated vesicle transport* (reactome, mean cos +0.51 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.57 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.55 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.1 | +1.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -11.1 | -10.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -9.1 | -8.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.4 | -9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | -4.8 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.2 | -4.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -4.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ARF GTPase activating protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:42,796,502-42,858,106 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARFGAP1 |
| Gene groups (HGNC) | ArfGAPs |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 14 pathways, smallest: RHOG GTPase cycle; COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP61](https://www.uniprot.org/uniprotkb/Q9NP61) (ADP-ribosylation factor GTPase-activating protein 3):

> GTPase-activating protein (GAP) for ADP ribosylation factor 1 (ARF1), which is essential for COPI vesicle formation and retrograde transport between the Golgi and the endoplasmic reticulum. Hydrolysis of ARF1-bound GTP leads to dissociation of coatomer from Golgi-derived membranes to allow fusion with target membranes. Promotes the proper assembly of the COPI coat lattice, rather than just acting as a simple curvature-dependent GAP like ARFGAP1.

**Summary**, from NCBI Gene [26286](https://www.ncbi.nlm.nih.gov/gene/26286):

> The protein encoded by this gene is a GTPase-activating protein (GAP) that associates with the Golgi apparatus and regulates the early secretory pathway of proteins. The encoded protein promotes hydrolysis of ADP-ribosylation factor 1 (ARF1)-bound GTP, which is required for the dissociation of coat proteins from Golgi-derived membranes and vesicles. Dissociation of the coat proteins is a prerequisite for the fusion of these vesicles with target compartments. The activity of this protein is …

**Accessions** — [HGNC:661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:661) · Entrez [26286](https://www.ncbi.nlm.nih.gov/gene/26286) · UniProt [Q9NP61](https://www.uniprot.org/uniprotkb/Q9NP61) · Ensembl [ENSG00000242247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242247)

## Data

Gene col 14308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14308); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14308]; `tensor/DDL_lfc|DDL_z.npy` [14308]; `embed/gene_vectors.npy` [14308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14308 or target_col == 14308). Every well: [[ARFGAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARFGAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
