---
symbol: "CCNY-AS1"
type: "gene"
col: 15681
ensembl_id: "ENSG00000271335"
name: "CCNY antisense RNA 1"
location: "10p11.21"
module: 15
arm: "+"
pooled_cpm: 16.25
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CCNY-AS1

*CCNY antisense RNA 1* — 10p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.61× (z +5.3, q 8e-05, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.431× (z -13.1, q 3e-36, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.489× (z -7.9, q 8e-13, down in 36 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HT-29 0.217×, PANC-1 0.334×, A498 0.272×, A549 0.234×, …; ⚠ cell-cycle shift, explains ~54% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (PANC-1 0.159×, LS 180 0.147×, NCI-H460 0.217×; ⚠ cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LS 180 0.0722×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.133×); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.282×); [[Celecoxib (drug)]] 0.5 µM in 1 line (Hs 766T 0.0771×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTC-338M12.4]] (+0.77, fdr 7e-06), [[LINC00115]] (+0.72, fdr 7e-06), [[CAPN10-DT]] (+0.72, fdr 7e-06); moves opposite to [[HES1]] (-0.66, fdr 7e-06), [[FOS]] (-0.60, fdr 1e-05), [[FOSB]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15681.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +5.3 | 8e-05 | 28/47 (LS 180, SHP-77, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +5.0 | 2e-04 | 31/48 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.4 | 0.002 | 17/41 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +4.2 | 0.004 | 23/48 (A498, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.029 | 21/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.068 | 13/48 (SNU-1, J82, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.068 | 17/47 (A549, SW1417, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.068 | 14/47 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.37× | +3.0 | 0.14 | 8/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.33× | +3.0 | 0.14 | 11/47 (NCI-H460, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15681.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (HT-29 0.217×, PANC-1 0.334×, A498 0.272×, A549 0.234×, …; ⚠ cell-cycle shift, explains ~54% of this change); [[Harringtonine (drug)]] 5 µM in 3 lines (PANC-1 0.159×, LS 180 0.147×, NCI-H460 0.217×; ⚠ cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LS 180 0.0722×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.133×); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.282×); [[Celecoxib (drug)]] 0.5 µM in 1 line (Hs 766T 0.0771×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.431×** | -13.1 | 3e-36 | 42/47 (HT-29, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.348×** | -11.1 | 2e-26 | 40/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.489×** | -7.9 | 8e-13 | 36/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.572×** | -6.1 | 1e-07 | 28/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.576×** | -6.1 | 2e-07 | 33/46 (LS 180, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.582×** | -5.9 | 3e-07 | 26/38 (LS 180, HT-29, …) | two highest doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.576×** | -5.8 | 5e-07 | 30/44 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.593×** | -5.7 | 8e-07 | 34/48 (HepG2/C3A, NCI-H460, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.520×** | -3.7 | 0.011 | 21/48 (NCI-H1792, NCI-H2347, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.524×** | -3.7 | 0.012 | 23/44 (A-427, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.724×** | -3.5 | 0.021 | 19/48 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.685×** | -3.5 | 0.023 | 18/47 (SNU-1, NCI-H661, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.718×** | -3.0 | 0.100 | 17/48 (SW480, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15681. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.229× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~51% of this change |
| [[A-172 (line)]] | wt | 22.9 | 0 | 3 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -12.1) ⚠ cell-cycle shift, explains ~84% of this change |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0722× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 17.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.217× (z -9.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.282× (z -8.5) |
| [[A549 (line)]] | wt | 12.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -10.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -11.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[J82 (line)]] | alt | 16.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.3) ⚠ cell-cycle shift, explains ~54% of this change |
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.4) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H2347 (line)]] | alt | 15.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 20.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.159× (z -12.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW480 (line)]] | alt | 14.1 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.274× (z -9.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HepG2_C3A (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 9.61 | 0 | 1 | — | [[Celecoxib (drug)]] 0.5 µM 0.0771× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 17.2 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.133× (z -8.9) |
| [[KATO III (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.187× (z -9.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.179× (z -9.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.128× (z -10.9) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0750× (z -8.5) ⚠ cell-cycle shift, explains ~79% of this change |
| [[SNU-423 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0719× (z -13.6) ⚠ toxic; cell-cycle shift, explains ~51% of this change |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -8.6) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A-427 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15681), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTC-338M12.4]] | +0.77 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[LINC00115]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[CAPN10-DT]] | +0.72 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[PGLS-DT]] | +0.70 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[NUDT16-DT]] | +0.70 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[FRG1HP]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[C8orf44-SGK3]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[VPS13B-DT]] | +0.68 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[GOT1-DT]] | +0.68 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[LINC01409]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[C8orf76]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[ZNF529-AS1]] | +0.65 | +0.46 / +0.71 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES1]] | -0.66 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[FOS]] | -0.60 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[FOSB]] | -0.57 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[PER2]] | -0.56 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[FAM222A]] | -0.53 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[SYAP1]] | -0.53 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[EGR2]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[NR4A1]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-8.0, 23.7); signed map (1.7, -0.7). **Vector** length 87.3, 19.1% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.6 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.0 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +0.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -6.4 | -11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -5.3 | -13.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.2 | -5.9 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.0 | -1.3 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -1.9 | -0.6 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.9 | -1.1 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | -1.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | CCNY antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p11.21 — chr10:35,314,552-35,336,401 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AL117336.3; previously LINC02634 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55252](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55252) · Entrez [118732302](https://www.ncbi.nlm.nih.gov/gene/118732302) · Ensembl [ENSG00000271335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271335)

## Data

Gene col 15681: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15681); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15681, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15681]; `tensor/DDL_lfc|DDL_z.npy` [15681]; `embed/gene_vectors.npy` [15681]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15681 or target_col == 15681). Every well: [[CCNY-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNY-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
