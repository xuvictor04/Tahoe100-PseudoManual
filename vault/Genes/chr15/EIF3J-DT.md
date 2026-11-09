---
symbol: "EIF3J-DT"
type: "gene"
col: 11038
ensembl_id: "ENSG00000179523"
name: "EIF3J divergent transcript"
location: "15q21.1"
module: 23
arm: "+"
pooled_cpm: 11.17
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# EIF3J-DT

*EIF3J divergent transcript* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +11.3, q 6e-27, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.594× (z -5.2, q 8e-05, down in 31 of 47 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.677× (z -3.9, q 0.015, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.143×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Bestatin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0531×); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0724×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (HS-578T 0.130×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OOEP]] (+0.80, fdr 7e-06), [[ATE1OSP]] (+0.78, fdr 7e-06), [[PCF11-AS1]] (+0.76, fdr 7e-06); moves opposite to [[SSX2IP]] (-0.67, fdr 2e-05), [[PRKDC]] (-0.67, fdr 1e-05), [[CS]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11038.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +11.3 | 6e-27 | 42/44 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.79×** | +8.2 | 5e-14 | 37/48 (Hs 766T, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.69×** | +5.2 | 3e-05 | 29/45 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.1 | 5e-05 | 26/41 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.8 | 1e-04 | 27/45 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +4.5 | 6e-04 | 22/47 (NCI-H460, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.2 | 0.002 | 13/22 (NCI-H1792, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +4.1 | 0.003 | 15/29 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.056 | 15/45 (HS-578T, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.056 | 16/47 (HS-578T, HEC-1-A, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.081 | 10/42 (A-427, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.081 | 17/46 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11038.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.143×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Bestatin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0531×); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0724×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (HS-578T 0.130×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.594×** | -5.2 | 8e-05 | 31/47 (SW480, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.596×** | -5.1 | 8e-05 | 27/47 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.672×** | -3.9 | 0.015 | 19/47 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.677×** | -3.9 | 0.015 | 18/47 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.685×** | -3.8 | 0.020 | 20/47 (LoVo, PANC-1, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.523×** | -3.4 | 0.069 | 17/44 (SNU-423, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 0.546× | -3.2 | 0.13 | 16/47 (KATO III, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.734× | -3.1 | 0.15 | 19/47 (MIA PaCa-2, LoVo, …) | inconsistent across doses | composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.739× | -3.0 | 0.17 | 11/48 (LS 180, RPMI-7951, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.88 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +21.2) | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 2 | — | [[Bestatin (drug)]] 5 µM 0.0531× (z -10.5) |
| [[A498 (line)]] | wt | 6.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 7.97 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.130× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 7.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +10.4) | — |
| [[SW480 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OOEP]] | +0.80 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.78 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[PCF11-AS1]] | +0.76 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[PIGP]] | +0.75 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[N4BP2L1]] | +0.72 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[NUTM2E]] | +0.72 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[SPEN-AS1]] | +0.71 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[PAXBP1-AS1]] | +0.71 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[LINC02951]] | +0.71 | +0.74 / +0.40 | both halves | 5e-05 |  |
| [[PPP1R42]] | +0.71 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.70 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[NDUFV2-AS1]] | +0.70 | +0.73 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | -0.67 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[PRKDC]] | -0.67 | -0.55 / -0.72 | both halves | 1e-05 |  |
| [[CS]] | -0.65 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[PDHA1]] | -0.64 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.64 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[PARP1]] | -0.64 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ICMT]] | -0.64 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[NCAPD3]] | -0.63 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[POLD2]] | -0.63 | -0.52 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises EIF3J-DT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers EIF3J-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[C10orf95-AS1]] | C | C10orf95-AS1 activity raises EIF3J-DT's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 1.21× lower at baseline in the lines without C10orf95-AS1 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.769). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (6.9, 21.5); signed map (30.3, -1.5). **Vector** length 87.7, 19.4% of its response variance represented; |z| ≥ 3 in 731 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +11.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.6 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +4.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.2 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -4.5 | -5.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -4.5 | -5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -4.4 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | EIF3J divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q21.1 — chr15:44,527,257-44,537,046 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously EIF3J-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48616) · Entrez [645212](https://www.ncbi.nlm.nih.gov/gene/645212) · Ensembl [ENSG00000179523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179523)

## Data

Gene col 11038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11038); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11038]; `tensor/DDL_lfc|DDL_z.npy` [11038]; `embed/gene_vectors.npy` [11038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11038 or target_col == 11038). Every well: [[EIF3J-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3J-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
