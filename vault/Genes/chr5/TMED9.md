---
symbol: "TMED9"
type: "gene"
col: 11581
ensembl_id: "ENSG00000184840"
name: "transmembrane p24 trafficking protein 9"
location: "5q35.3"
module: 42
arm: "+"
pooled_cpm: 121.8
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TMED9

*transmembrane p24 trafficking protein 9* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.40× (z +8.3, q 8e-14, up in 44 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A-172 3.33×, HOP62 3.50×, C-33 A 4.41×, LOX-IMVI 4.05×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 4.12×, HOP62 3.01×, A-427 2.74×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.504× (z -9.6, q 4e-19, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P4HB]] (+0.85, fdr 7e-06), [[MYDGF]] (+0.80, fdr 7e-06), [[MANF]] (+0.80, fdr 7e-06); moves opposite to [[USP24]] (-0.64, fdr 4e-05), [[RIF1]] (-0.64, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CPEB1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[COPE]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11581.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A-172 3.33×, HOP62 3.50×, C-33 A 4.41×, LOX-IMVI 4.05×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 4.12×, HOP62 3.01×, A-427 2.74×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.40×** | +8.3 | 8e-14 | 44/49 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.97×** | +6.5 | 3e-08 | 40/44 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.58×** | +4.6 | 0.001 | 43/48 (HOP62, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.57×** | +4.1 | 0.006 | 33/45 (SNU-423, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.57× | +3.1 | 0.18 | 39/48 (RKO, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.37× | +3.1 | 0.18 | 27/48 (LOX-IMVI, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11581.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.504×** | -9.6 | 4e-19 | 46/48 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.659×** | -4.0 | 0.019 | 34/48 (NCI-H2347, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.779×** | -3.5 | 0.080 | 29/48 (H4, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Budesonide (drug)]] 5 µM |  | **0.707×** | -3.4 | 0.080 | 37/48 (H4, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.724× | -3.2 | 0.15 | 27/48 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.646× | -3.0 | 0.17 | 32/48 (HS-578T, J82, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.738× | -3.0 | 0.17 | 33/48 (HS-578T, J82, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.729× | -3.0 | 0.17 | 29/49 (SW 1088, H4, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 93.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -10.2) |
| [[HOP62 (line)]] | alt | 168 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.8) |
| [[A-172 (line)]] | wt | 167 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.6) |
| [[C-33 A (line)]] | alt | 74.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 178 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 145 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -9.8) |
| [[SNU-423 (line)]] | alt | 98.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW 1088 (line)]] | alt | 287 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -11.3) |
| [[A498 (line)]] | wt | 192 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 118 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.2) |
| [[H4 (line)]] | wt | 262 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.0) |
| [[HS-578T (line)]] | alt | 257 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 159 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.6) |
| [[J82 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -15.6) |
| [[KATO III (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.5) |
| [[LoVo (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 58.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 98.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 129 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -12.9) |
| [[SW1417 (line)]] | alt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -13.6) |
| [[SW48 (line)]] | wt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.6) |
| [[A549 (line)]] | wt | 100.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 124 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 94.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 117 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 120 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 83.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 83.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P4HB]] | +0.85 | +0.84 / +0.78 | both halves | 7e-06 | STRING 499 |
| [[MYDGF]] | +0.80 | +0.85 / +0.80 | both halves | 7e-06 | STRING 607 |
| [[MANF]] | +0.80 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[PDIA4]] | +0.80 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[SLC31A1]] | +0.79 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[SSR2]] | +0.79 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[SEC61B]] | +0.79 | +0.76 / +0.80 | both halves | 7e-06 | STRING 470 |
| [[KDELR2]] | +0.79 | +0.78 / +0.79 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 596 |
| [[PPIB]] | +0.79 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[HSP90B1]] | +0.78 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[HM13]] | +0.78 | +0.76 / +0.76 | both halves | 7e-06 | STRING 402 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP24]] | -0.64 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[RIF1]] | -0.64 | -0.55 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPEB1]] | B | CPEB1 activity raises TMED9's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 1.33× lower at baseline in the lines without CPEB1 | 0.075 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COPE]] | C | TMED9's natural level weakens COPE's drug response | TMED9's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.11; direction not clear | 0.068 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.794). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, -32.4); signed map (-52.8, 8.9). **Vector** length 107, 44.4% of its response variance represented; |z| ≥ 3 in 604 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.69 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.60 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.58 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.5 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.0 | -9.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -4.9 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -0.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.6 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane p24 trafficking protein 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,592,203-177,597,242 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSGP25L2G, p24alpha2, p24a2 |
| Gene groups (HGNC) | Transmembrane p24 trafficking proteins |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVK6](https://www.uniprot.org/uniprotkb/Q9BVK6) (Transmembrane emp24 domain-containing protein 9):

> Appears to be involved in vesicular protein trafficking, mainly in the early secretory pathway. In COPI vesicle-mediated retrograde transport involved in the coatomer recruitment to membranes of the early secretory pathway. Increases coatomer-dependent activity of ARFGAP2. Thought to play a crucial role in the specific retention of p24 complexes in cis-Golgi membranes; specifically contributes to the coupled localization of TMED2 and TMED10 in the cis-Golgi network. May be involved in …

**Summary**, from NCBI Gene [54732](https://www.ncbi.nlm.nih.gov/gene/54732):

> This gene is a member of a family of genes encoding transport proteins located in the endoplasmic reticulum and the Golgi. A similar gene in mouse is the target of microRNA miR-296, which is part of an imprinted cluster. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:24878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24878) · Entrez [54732](https://www.ncbi.nlm.nih.gov/gene/54732) · UniProt [Q9BVK6](https://www.uniprot.org/uniprotkb/Q9BVK6) · Ensembl [ENSG00000184840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184840)

## Data

Gene col 11581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11581); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11581]; `tensor/DDL_lfc|DDL_z.npy` [11581]; `embed/gene_vectors.npy` [11581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11581 or target_col == 11581). Every well: [[TMED9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMED9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
