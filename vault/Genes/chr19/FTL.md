---
symbol: "FTL"
type: "gene"
col: 1481
ensembl_id: "ENSG00000087086"
name: "ferritin light chain"
location: "19q13.33"
module: 43
arm: "+"
pooled_cpm: 708.34
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# FTL

*ferritin light chain* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.27× (z +8.0, q 8e-13, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.431× (z -6.6, q 2e-08, down in 44 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (HT-29 0.233×, HCT15 0.196×, NCI-H2347 0.185×, SHP-77 0.195×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED31]] (+0.73, fdr 7e-06), [[RPLP1]] (+0.70, fdr 7e-06), [[RPS20]] (+0.69, fdr 7e-06); moves opposite to [[CHAMP1]] (-0.68, fdr 7e-06), [[SF3B3]] (-0.68, fdr 7e-06), [[HNRNPD]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1481.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.27×** | +8.0 | 8e-13 | 46/47 (Panc 03.27, AsPC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.47×** | +6.9 | 2e-09 | 48/48 (C-33 A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.18×** | +6.4 | 4e-08 | 46/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.32×** | +6.2 | 6e-08 | 46/47 (HT-29, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.09×** | +6.2 | 6e-08 | 46/47 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +5.4 | 6e-06 | 42/43 (C-33 A, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.19×** | +4.1 | 0.003 | 42/44 (A-172, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.87×** | +3.4 | 0.044 | 42/47 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.4 | 0.045 | 38/46 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +3.3 | 0.059 | 34/44 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.48× | +3.1 | 0.12 | 41/47 (HT-29, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1481.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (HT-29 0.233×, HCT15 0.196×, NCI-H2347 0.185×, SHP-77 0.195×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.431×** | -6.6 | 2e-08 | 44/47 (HT-29, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | 0.515× | -3.5 | 0.12 | 31/47 (HCT15, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 5 µM |  | 0.580× | -3.0 | 0.44 | 41/47 (SW 900, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 1,372 | 4 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 6.46× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 581 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.11× (z +10.6) | — |
| [[SW480 (line)]] | alt | 317 | 4 | 0 | [[Auranofin (drug)]] 5 µM 6.93× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 412 | 3 | 0 | [[Auranofin (drug)]] 5 µM 11.1× (z +12.0) | — |
| [[HCT15 (line)]] | alt | 626 | 2 | 1 | [[Auranofin (drug)]] 5 µM 6.29× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.9) |
| [[KATO III (line)]] | alt | 682 | 3 | 0 | [[Auranofin (drug)]] 5 µM 5.49× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 253 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 10.0× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -10.8) |
| [[AN3 CA (line)]] | alt | 305 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.99× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 180 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 436 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.23× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 881 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.60× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 368 | 2 | 0 | [[Auranofin (drug)]] 5 µM 12.1× (z +13.6) | — |
| [[A549 (line)]] | wt | 962 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.82× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 454 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.21× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 673 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.95× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 317 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 884 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 189 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.0× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 546 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.25× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 593 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.94× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 710 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.94× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 1,656 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 660 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.40× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 833 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -8.8) |
| [[SHP-77 (line)]] | alt | 372 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 494 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -8.8) |
| [[SW 1271 (line)]] | alt | 281 | 1 | 0 | [[Auranofin (drug)]] 5 µM 13.8× (z +11.2) | — |
| [[A-172 (line)]] | wt | 315 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 712 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1,235 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 168 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 299 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1,574 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 272 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 677 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 794 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1,552 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 776 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1,565 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 642 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 619 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 471 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 525 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 862 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 784 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 717 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1,438 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 227 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 11 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED31]] | +0.73 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[RPLP1]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[RPS20]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[UBA52]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 | pathway: Iron uptake and transport |
| [[CAMLG]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[PFDN5]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[RPS12]] | +0.68 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[RPS27]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 | STRING 431 |
| [[RAD9A]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[RPL35A]] | +0.67 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[BLVRB]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[RPS8]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHAMP1]] | -0.68 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[SF3B3]] | -0.68 | -0.60 / -0.71 | both halves | 7e-06 |  |
| [[HNRNPD]] | -0.65 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[PFAS]] | -0.63 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[VARS1]] | -0.63 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[LMNB2]] | -0.62 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[NUP188]] | -0.62 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[PHF19]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[SYNCRIP]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.60 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[DNMT1]] | -0.60 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[NHLRC2]] | -0.59 | -0.46 / -0.67 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers FTL's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[VEGFD]] | B | VEGFD activity lowers FTL's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.12× higher at baseline in the lines without VEGFD | 0.094 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-43.3, -27.7); signed map (-25.1, 9.7). **Vector** length 116, 60.1% of its response variance represented; |z| ≥ 3 in 723 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.56 to 55); *Peptide chain elongation* (reactome, mean cos +0.56 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.55 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.7 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.5 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.8 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +8.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.3 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.7 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +1.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.3 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -10.2 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.7 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -0.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.5 | +1.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.3 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | ferritin light chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,965,309-48,966,879 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC71996, NBIA3, FTL1 |
| Gene groups (HGNC) | Ferritin chains |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Reactome | 10 pathways, smallest: Scavenging by Class A Receptors; Binding and Uptake of Ligands by Scavenger Receptors; Iron uptake and transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P02792](https://www.uniprot.org/uniprotkb/P02792) (Ferritin light chain):

> Stores iron in a soluble, non-toxic, readily available form. Important for iron homeostasis. Iron is taken up in the ferrous form and deposited as ferric hydroxides after oxidation. Also plays a role in delivery of iron to cells. Mediates iron uptake in capsule cells of the developing kidney (By similarity). Delivery to lysosomes by the cargo receptor NCOA4 for autophagic degradation and release or iron.

**Summary**, from NCBI Gene [2512](https://www.ncbi.nlm.nih.gov/gene/2512):

> This gene encodes the light subunit of the ferritin protein. Ferritin is the major intracellular iron storage protein in prokaryotes and eukaryotes. It is composed of 24 subunits of the heavy and light ferritin chains. Variation in ferritin subunit composition may affect the rates of iron uptake and release in different tissues. A major function of ferritin is the storage of iron in a soluble and nontoxic state. Defects in this light chain ferritin gene are associated with several …

**Accessions** — [HGNC:3999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3999) · Entrez [2512](https://www.ncbi.nlm.nih.gov/gene/2512) · UniProt [P02792](https://www.uniprot.org/uniprotkb/P02792) · Ensembl [ENSG00000087086](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087086)

## Data

Gene col 1481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1481); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1481]; `tensor/DDL_lfc|DDL_z.npy` [1481]; `embed/gene_vectors.npy` [1481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1481 or target_col == 1481). Every well: [[FTL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FTL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
