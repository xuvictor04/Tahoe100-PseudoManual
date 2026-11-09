---
symbol: "RPA2"
type: "gene"
col: 3947
ensembl_id: "ENSG00000117748"
name: "replication protein A2"
location: "1p35.3"
module: 6
arm: "+"
pooled_cpm: 22.39
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RPA2

*replication protein A2* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.13× (z +12.9, q 2e-35, up in 26 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.40× (z +6.0, q 3e-07, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.767× (z -6.7, q 1e-08, down in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.500×, SNU-1 0.275×, A-427 0.441×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.273×, NCI-H23 0.467×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.223×, C-33 A 0.256×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SNU-1 0.0578×); [[Asciminib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0654×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP107]] (+0.72, fdr 7e-06), [[CNOT10]] (+0.70, fdr 7e-06), [[POLA2]] (+0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DSCC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 20 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3947.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.13×** | +12.9 | 2e-35 | 26/32 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.00×** | +12.4 | 1e-32 | 35/42 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.47×** | +6.7 | 5e-09 | 29/48 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.43×** | +6.2 | 1e-07 | 22/47 (SW 900, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +6.0 | 3e-07 | 23/48 (LOX-IMVI, PANC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.35×** | +5.4 | 6e-06 | 21/48 (PANC-1, SHP-77, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.37×** | +5.4 | 6e-06 | 20/43 (PANC-1, C-33 A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.33×** | +5.1 | 3e-05 | 16/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.32×** | +5.0 | 3e-05 | 20/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.32×** | +4.8 | 8e-05 | 21/48 (NCI-H2030, LoVo, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.68×** | +4.8 | 1e-04 | 19/48 (LoVo, KATO III, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.20× | +4.6 | 2e-04 | 18/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **1.30×** | +4.5 | 3e-04 | 16/46 (A-427, H4, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **1.28×** | +4.5 | 3e-04 | 20/46 (A-427, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +4.4 | 3e-04 | 14/48 (LoVo, LS 180, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.013 | 13/48 (SW480, J82, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.061 | 5/47 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.26×** | +2.9 | 0.092 | 2/48 (MIA PaCa-2, NCI-H2347) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3947.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.500×, SNU-1 0.275×, A-427 0.441×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.273×, NCI-H23 0.467×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.223×, C-33 A 0.256×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SNU-1 0.0578×); [[Asciminib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0654×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.767×** | -6.7 | 1e-08 | 25/47 (A498, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -4.1 | 0.010 | 4/48 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.730×** | -4.0 | 0.013 | 10/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.873× | -3.4 | 0.090 | 14/48 (KATO III, Panc 03.27, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.837× | -3.2 | 0.17 | 14/48 (A498, A-427, …) | all doses, flat | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.839× | -3.1 | 0.17 | 14/47 (A-172, A549, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 27.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -17.4) |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 2 (1 ⚠) | — | [[Pyridoxine (drug)]] 0.5 µM 0.0578× (z -13.7) |
| [[A-427 (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.441× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 58.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HepG2_C3A (line)]] | wt | 7.81 | 0 | 1 | — | [[Asciminib (drug)]] 0.05 µM 0.0654× (z -9.3) |
| [[LS 180 (line)]] | wt | 11.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H23 (line)]] | alt | 41.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[SW480 (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP107]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CNOT10]] | +0.70 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[POLA2]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 940 |
| [[ATAD5]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[WDHD1]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 | STRING 480 |
| [[ZGRF1]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[MTBP]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[GINS1]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CDC45]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 899 |
| [[RBL1]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[MCM10]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 624 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSCC1]] | C | DSCC1 activity raises RPA2's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.77× lower at baseline in the lines without DSCC1 | 0.068 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises RPA2's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without MYBL2 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.1, -47.3); signed map (-40.7, -44.6). **Vector** length 78.1, 14.9% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.51 to 23); *Unwinding of DNA* (reactome, mean cos +0.56 to 12); *Leading Strand Synthesis* (reactome, mean cos +0.56 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.1 | +5.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.6 | +4.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | +0.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +6.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.4 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | replication protein A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:27,891,524-27,914,746 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Nucleotide excision repair |
| Hallmark sets | DNA_REPAIR, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 71 pathways, smallest: Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta); Mismatch repair (MMR) directed by MSH2:MSH6 (MutSalpha); Removal of the Flap Intermediate |
| Matched by | ensembl_id |

**Function**, from UniProt [P15927](https://www.uniprot.org/uniprotkb/P15927) (Replication protein A 32 kDa subunit):

> As part of the heterotrimeric replication protein A complex (RPA/RP-A), binds and stabilizes single-stranded DNA intermediates that form during DNA replication or upon DNA stress. It prevents their reannealing and in parallel, recruits and activates different proteins and complexes involved in DNA metabolism. Thereby, it plays an essential role both in DNA replication and the cellular response to DNA damage. In the cellular response to DNA damage, the RPA complex controls DNA repair and DNA …

**Summary**, from NCBI Gene [6118](https://www.ncbi.nlm.nih.gov/gene/6118):

> This gene encodes a subunit of the heterotrimeric Replication Protein A (RPA) complex, which binds to single-stranded DNA (ssDNA), forming a nucleoprotein complex that plays an important role in DNA metabolism, being involved in DNA replication, repair, recombination, telomere maintenance, and co-ordinating the cellular response to DNA damage through activation of the ataxia telangiectasia and Rad3-related protein (ATR) kinase. The RPA complex protects single-stranded DNA from nucleases, …

**Accessions** — [HGNC:10290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10290) · Entrez [6118](https://www.ncbi.nlm.nih.gov/gene/6118) · UniProt [P15927](https://www.uniprot.org/uniprotkb/P15927) · Ensembl [ENSG00000117748](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117748)

## Data

Gene col 3947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3947); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3947]; `tensor/DDL_lfc|DDL_z.npy` [3947]; `embed/gene_vectors.npy` [3947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3947 or target_col == 3947). Every well: [[RPA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
