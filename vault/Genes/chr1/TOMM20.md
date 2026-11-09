---
symbol: "TOMM20"
type: "gene"
col: 10423
ensembl_id: "ENSG00000173726"
name: "translocase of outer mitochondrial membrane 20"
location: "1q42.3"
module: 43
arm: "+"
pooled_cpm: 193.59
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# TOMM20

*translocase of outer mitochondrial membrane 20* — 1q42.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.41× (z +8.3, q 7e-14, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.61× (z +5.3, q 2e-05, up in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H1792 4.80×, A549 4.21×, A498 3.37×, HT-29 3.08×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 3.56×, NCI-H1792 3.59×, A498 2.71×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 4.36×, SW480 2.33×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (CHP-212 0.364×, SW480 0.528×, RKO 0.463×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (CHP-212 0.467×, HepG2/C3A 0.483×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL5]] (+0.75, fdr 7e-06), [[RPS3]] (+0.73, fdr 7e-06, ⚠ RPS3 in the vector space only through flagged drug-doses), [[RPL13]] (+0.71, fdr 7e-06), [[RPS5]] (+0.71, fdr 1e-05); moves opposite to [[EIF4G2]] (-0.67, fdr 1e-05), [[PSME3IP1]] (-0.66, fdr 2e-05), [[ZNF681]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10423.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H1792 4.80×, A549 4.21×, A498 3.37×, HT-29 3.08×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 3.56×, NCI-H1792 3.59×, A498 2.71×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 4.36×, SW480 2.33×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.41×** | +8.3 | 7e-14 | 47/49 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.01×** | +7.4 | 4e-11 | 44/44 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.83×** | +6.2 | 1e-07 | 39/45 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.64×** | +5.5 | 7e-06 | 42/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +5.3 | 2e-05 | 43/48 (A-172, C-33 A, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.47×** | +4.3 | 0.002 | 37/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.46×** | +4.2 | 0.002 | 38/48 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.42×** | +3.9 | 0.008 | 40/48 (COLO 205, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.39×** | +3.6 | 0.017 | 32/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.36×** | +3.4 | 0.039 | 30/48 (NCI-H460, SW480, …) | rises with dose | composition shift |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (CHP-212 0.364×, SW480 0.528×, RKO 0.463×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (CHP-212 0.467×, HepG2/C3A 0.483×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 262 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.36× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SW480 (line)]] | alt | 195 | 3 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.33× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 204 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 169 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[CHP-212 (line)]] | wt | 425 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 232 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.94× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 159 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 181 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 152 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 175 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 196 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 249 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 173 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 191 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 226 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 130 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 194 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 190 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 200 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 183 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 225 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 17 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL5]] | +0.75 | +0.66 / +0.77 | both halves | 7e-06 | same gene group; pathway: Protein localization |
| [[RPS3]] ⚠ | +0.73 | +0.69 / +0.70 | both halves | 7e-06 | same gene group; pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[RPL13]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 | same gene group; pathway: Protein localization |
| [[RPS5]] | +0.71 | +0.56 / +0.66 | both halves | 1e-05 | pathway: Protein localization |
| [[RPS6]] ⚠ | +0.71 | +0.65 / +0.73 | both halves | 7e-06 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[RPL11]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 | pathway: Protein localization |
| [[RPL31]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 | pathway: Protein localization |
| [[RPS14]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 | pathway: Protein localization |
| [[RPL34]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 | pathway: Protein localization |
| [[RPS16]] ⚠ | +0.69 | +0.62 / +0.61 | both halves | 7e-06 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[RPS25]] | +0.69 | +0.59 / +0.65 | both halves | 7e-06 | pathway: Protein localization |
| [[RPL32]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 | same gene group; pathway: Protein localization |
| [[RPS10]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 | pathway: Protein localization |
| [[RACK1]] | +0.68 | +0.58 / +0.67 | both halves | 8e-06 | same gene group |
| [[RPL27]] | +0.68 | +0.60 / +0.64 | both halves | 7e-06 | pathway: Protein localization |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.67 | -0.55 / -0.50 | both halves | 1e-05 | same gene group |
| [[PSME3IP1]] | -0.66 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ZNF681]] | -0.65 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[FAM111A]] | -0.64 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[ATXN7]] | -0.64 | -0.42 / -0.49 | both halves | 4e-05 | pathway: Deubiquitination |
| [[MSANTD7]] | -0.62 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[C5orf15]] | -0.62 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[TOR1A]] | -0.61 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[PBLD]] | -0.61 | -0.40 / -0.23 | both halves | 5e-04 |  |
| [[ZBED5]] | -0.61 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[C7orf25]] | -0.61 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ZNF747]] | -0.61 | -0.44 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TOMM20's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RGS10]] | C | RGS10 activity raises TOMM20's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.32× lower at baseline in the lines without RGS10 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.1, -28.1); signed map (-61.0, -4.4). **Vector** length 96.8, 42.1% of its response variance represented; |z| ≥ 3 in 690 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.60 to 55); *Peptide chain elongation* (reactome, mean cos +0.61 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.60 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.3 | +4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.0 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.7 | +3.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +1.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.8 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.2 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.6 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -0.8 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | translocase of outer mitochondrial membrane 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.3 — chr1:235,109,341-235,128,837 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0016, TOM20, MOM19, MAS20 |
| Gene groups (HGNC) | Translocase of outer mitochondrial membrane complex; Small nucleolar RNA protein coding host genes |
| Reactome | 9 pathways, smallest: PINK1-PRKN Mediated Mitophagy; Mitophagy; Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15388](https://www.uniprot.org/uniprotkb/Q15388) (Mitochondrial import receptor subunit TOM20 homolog):

> Central receptor component of the translocase of the outer membrane of mitochondria (TOM) complex essential for the recognition and translocation of cytosolically synthesized mitochondrial preproteins. Together with TOMM22 functions as the transit peptide receptor at the surface of the mitochondrion outer membrane and facilitates the movement of preproteins into the TOM40 translocation pore. The TOM complex associates with the ion channel VDAC2 and PINK1 kinase at depolarized mitochondria, this …

**Summary**, from NCBI Gene [9804](https://www.ncbi.nlm.nih.gov/gene/9804):

> Enables mitochondrion targeting sequence binding activity; protein-transporting ATPase activity; and unfolded protein binding activity. Involved in obsolete protein targeting to mitochondrion. Located in mitochondria-associated endoplasmic reticulum membrane contact site and mitochondrial outer membrane. Is active in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20947) · Entrez [9804](https://www.ncbi.nlm.nih.gov/gene/9804) · UniProt [Q15388](https://www.uniprot.org/uniprotkb/Q15388) · Ensembl [ENSG00000173726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173726)

## Data

Gene col 10423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10423); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10423]; `tensor/DDL_lfc|DDL_z.npy` [10423]; `embed/gene_vectors.npy` [10423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10423 or target_col == 10423). Every well: [[TOMM20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOMM20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
