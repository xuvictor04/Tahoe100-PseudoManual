---
symbol: "ANTKMT"
type: "gene"
col: 2344
ensembl_id: "ENSG00000103254"
name: "adenine nucleotide translocase lysine methyltransferase"
location: "16p13.3"
module: 58
arm: "+"
pooled_cpm: 3.33
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# ANTKMT

*adenine nucleotide translocase lysine methyltransferase* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.11× (z +9.1, q 7e-17, up in 17 of 18 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.563× (z -5.2, q 1e-04, down in 21 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.0696×, NCI-H460 0.0716×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (SW48 0.0410×; ⚠ cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.0421×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM160]] (+0.80, fdr 7e-06), [[PAFAH1B3]] (+0.78, fdr 2e-05), [[PUSL1]] (+0.75, fdr 3e-05); moves opposite to [[EIF4G2]] (-0.66, fdr 3e-04), [[VPS52]] (-0.66, fdr 3e-04), [[ATXN1L]] (-0.64, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 9 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **4.11×** | +9.1 | 7e-17 | 17/18 (A498, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.77×** | +8.2 | 8e-14 | 2/4 (A498, PANC-1) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.78×** | +6.1 | 3e-07 | 4/5 (A498, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.46×** | +5.8 | 1e-06 | 29/42 (SW480, NCI-H460, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **2.28×** | +5.3 | 1e-05 | 14/21 (NCI-H2347, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.94×** | +4.3 | 0.002 | 25/45 (SW480, KATO III, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.90×** | +4.1 | 0.003 | 14/44 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.5 | 0.034 | 4/20 (SW1417, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +3.2 | 0.083 | 7/47 (HEC-1-A, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2344.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.0696×, NCI-H460 0.0716×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (SW48 0.0410×; ⚠ cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW48 0.0421×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.563×** | -5.2 | 1e-04 | 21/36 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.597× | -3.2 | 0.36 | 19/42 (SNU-1, RKO, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.614× | -3.1 | 0.36 | 14/33 (SW48, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 11.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0410× (z -10.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0421× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 5.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0696× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 2.38 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0716× (z -12.1) |
| [[A-172 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 15 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM160]] | +0.80 | +0.61 / +0.77 | both halves | 7e-06 | STRING 436 |
| [[PAFAH1B3]] | +0.78 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[PUSL1]] | +0.75 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[LAGE3]] | +0.73 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[MICOS13]] | +0.73 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[MRPL41]] ⚠ | +0.73 | +0.47 / +0.67 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5F1D]] ⚠ | +0.72 | +0.24 / +0.71 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL12]] | +0.71 | +0.37 / +0.71 | both halves | 7e-05 |  |
| [[PAXX]] ⚠ | +0.71 | +0.30 / +0.68 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[HAGHL]] | +0.71 | +0.54 / +0.73 | both halves | 1e-05 | STRING 522; ⚠ same locus (4.3 kb, same strand: neighbours can correlate without regulation) |
| [[TMEM276]] | +0.71 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[TMEM256]] | +0.70 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[NDUFA3]] | +0.70 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[MRPL14]] | +0.68 | +0.28 / +0.62 | both halves | 3e-04 |  |
| [[CISD3]] | +0.68 | +0.43 / +0.68 | both halves | 4e-05 |  |
| [[C20orf27]] | +0.68 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.66 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[VPS52]] | -0.66 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[ATXN1L]] | -0.64 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[PNISR-AS1]] | -0.64 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[CHD3]] | -0.63 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[DHX38]] | -0.62 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[PBLD]] | -0.62 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[PSME3IP1]] | -0.62 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[MMADHC-DT]] | -0.60 | -0.45 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[DDX39B]] | -0.60 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.60 | -0.50 / -0.22 | both halves | 6e-04 |  |
| [[PRKAR1A]] | -0.59 | -0.14 / -0.61 | ⚠ one half (not replicated) | 0.002 |  |
| [[RNF6]] | -0.59 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[GLIPR1-AS1]] | -0.59 | -0.35 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ANTKMT's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HES6]] | B | HES6 activity raises ANTKMT's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without HES6 | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HLA-K]] | B | HLA-K activity lowers ANTKMT's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.28× higher at baseline in the lines without HLA-K | 0.098 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.916). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.6, -15.5); signed map (-31.8, 4.2). **Vector** length 47.4, 6.80% of its response variance represented; |z| ≥ 3 in 748 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *oxidative phosphorylation* (hallmark, mean cos +0.55 to 12); *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.56 to 12); *Complex I biogenesis* (reactome, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.8 | +5.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.8 | +4.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.2 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Bendamustine (drug)]] 5 µM |  | +1.0 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.0 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.1 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | adenine nucleotide translocase lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:720,581-722,590 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2494; previously C16orf24, FAM173A |
| Gene groups (HGNC) | 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQD7](https://www.uniprot.org/uniprotkb/Q9BQD7) (Adenine nucleotide translocase lysine N-methyltransferase):

> Mitochondrial protein-lysine N-methyltransferase that trimethylates adenine nucleotide translocases ANT2/SLC25A5 and ANT3/SLC25A6, thereby regulating mitochondrial respiration. Probably also trimethylates ANT1/SLC25A4.

**Summary**, from NCBI Gene [65990](https://www.ncbi.nlm.nih.gov/gene/65990):

> Enables protein-lysine N-methyltransferase activity. Involved in peptidyl-lysine trimethylation. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14152) · Entrez [65990](https://www.ncbi.nlm.nih.gov/gene/65990) · UniProt [Q9BQD7](https://www.uniprot.org/uniprotkb/Q9BQD7) · Ensembl [ENSG00000103254](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103254)

## Data

Gene col 2344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2344); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2344]; `tensor/DDL_lfc|DDL_z.npy` [2344]; `embed/gene_vectors.npy` [2344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2344 or target_col == 2344). Every well: [[ANTKMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANTKMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
