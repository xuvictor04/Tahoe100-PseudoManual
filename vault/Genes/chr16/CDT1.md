---
symbol: "CDT1"
type: "gene"
col: 9474
ensembl_id: "ENSG00000167513"
name: "chromatin licensing and DNA replication factor 1"
location: "16q24.3"
module: 6
arm: "+"
pooled_cpm: 10.96
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CDT1

*chromatin licensing and DNA replication factor 1* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.74× (z +4.6, q 0.003, up in 20 of 36 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Betamethasone dipropionate (drug)]] 5 µM: 1.66× (z +4.0, q 0.013, up in 16 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.451× (z -9.2, q 2e-17, down in 40 of 45 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.613× (z -4.0, q 0.009, down in 19 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 6 lines (A498 0.180×, NCI-H460 0.131×, LoVo 0.153×, A-172 0.173×, …; ⚠ cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H23 0.119×, MIA PaCa-2 0.137×, SW480 0.311×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.142×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (COLO 205 0.0843×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 0.355×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLM]] (+0.78, fdr 7e-06), [[DTL]] (+0.74, fdr 7e-06), [[CDCA5]] (+0.74, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.74×** | +4.6 | 0.003 | 20/36 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.43×** | +4.2 | 0.009 | 20/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.013 | 16/44 (PANC-1, SW1417, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.38×** | +3.7 | 0.030 | 18/46 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.33× | +3.3 | 0.11 | 15/44 (SW480, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.48× | +3.2 | 0.11 | 15/46 (RKO, A549, …) | two highest doses | position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.46× | +3.1 | 0.17 | 11/42 (NCI-H2347, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9474.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 6 lines (A498 0.180×, NCI-H460 0.131×, LoVo 0.153×, A-172 0.173×, …; ⚠ cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H23 0.119×, MIA PaCa-2 0.137×, SW480 0.311×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.142×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (COLO 205 0.0843×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 0.355×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.451×** | -9.2 | 2e-17 | 40/45 (A498, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.545×** | -5.0 | 2e-04 | 25/43 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.343×** | -4.9 | 2e-04 | 27/47 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.613×** | -4.0 | 0.009 | 19/40 (NCI-H460, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.89 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 24.4 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.180× (z -14.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.355× (z -8.9) |
| [[A-172 (line)]] | wt | 14.6 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.173× (z -11.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.209× (z -9.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -11.8) |
| [[COLO 205 (line)]] | alt | 6.12 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.0843× (z -9.2) |
| [[LoVo (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.153× (z -11.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0960× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 7.12 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.131× (z -12.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.294× (z -9.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW480 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.5) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLM]] | +0.78 | +0.77 / +0.73 | both halves | 7e-06 | STRING 502 |
| [[DTL]] | +0.74 | +0.74 / +0.74 | both halves | 7e-06 | STRING 998 |
| [[CDCA5]] | +0.74 | +0.76 / +0.76 | both halves | 7e-06 | pathway: S Phase; STRING 842 |
| [[RBL1]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 | pathway: G1/S Transition |
| [[EXO1]] | +0.73 | +0.79 / +0.69 | both halves | 7e-06 | STRING 870 |
| [[RFC2]] | +0.73 | +0.68 / +0.74 | both halves | 7e-06 | pathway: DNA Replication; STRING 639 |
| [[PKMYT1]] | +0.72 | +0.76 / +0.74 | both halves | 7e-06 | STRING 659 |
| [[HAUS8]] | +0.72 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[FANCB]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[PRIM1]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 | pathway: Activation of the pre-replicative complex; STRING 652 |
| [[POLQ]] | +0.71 | +0.75 / +0.68 | both halves | 7e-06 | STRING 464 |
| [[ORC6]] | +0.71 | +0.68 / +0.81 | both halves | 7e-06 | pathway: Activation of the pre-replicative complex; STRING 997 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises CDT1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.50× lower at baseline in the lines without TCF19 | 0.031 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises CDT1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.21× lower at baseline in the lines without E2F8 | 0.033 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises CDT1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.94× lower at baseline in the lines without E2F2 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CDT1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.45× lower at baseline in the lines without AURKB | 0.037 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MELK]], [[TK1]] | C | MELK, TK1 activity raises CDT1's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 2.68× lower at baseline in the lines without MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[MCM10]] | C | MCM10 activity raises CDT1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without MCM10 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F1]] | C | E2F1 activity raises CDT1's level | lines that do not express E2F1 (3) vs lines expressing it (47) | 2.39× lower at baseline in the lines without E2F1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.2, -48.7); signed map (-42.0, -43.2). **Vector** length 98.3, 27.3% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.50 to 65); *DNA strand elongation* (reactome, mean cos +0.56 to 28); *Cell Cycle Checkpoints* (reactome, mean cos +0.56 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.2 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.1 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +2.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.3 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.7 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -7.7 | -9.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -5.5 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.7 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.3 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | chromatin licensing and DNA replication factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:88,803,789-88,809,258 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DUP, RIS2 |
| Reactome | 13 pathways, smallest: G1/S-Specific Transcription; Activation of the pre-replicative complex; Orc1 removal from chromatin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H211](https://www.uniprot.org/uniprotkb/Q9H211) (DNA replication factor Cdt1):

> Required for both DNA replication and mitosis. DNA replication licensing factor, required for pre-replication complex assembly. Cooperates with CDC6 and the origin recognition complex (ORC) during G1 phase of the cell cycle to promote the loading of the mini-chromosome maintenance (MCM) complex onto DNA to generate pre-replication complexes (pre-RC). Required also for mitosis by promoting stable kinetochore-microtubule attachments. Potential oncogene (By similarity).

**Summary**, from NCBI Gene [81620](https://www.ncbi.nlm.nih.gov/gene/81620):

> The protein encoded by this gene is involved in the formation of the pre-replication complex that is necessary for DNA replication. The encoded protein can bind geminin, which prevents replication and may function to prevent this protein from initiating replication at inappropriate origins. Phosphorylation of this protein by cyclin A-dependent kinases results in degradation of the protein. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:24576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24576) · Entrez [81620](https://www.ncbi.nlm.nih.gov/gene/81620) · UniProt [Q9H211](https://www.uniprot.org/uniprotkb/Q9H211) · Ensembl [ENSG00000167513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167513)

## Data

Gene col 9474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9474); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9474]; `tensor/DDL_lfc|DDL_z.npy` [9474]; `embed/gene_vectors.npy` [9474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9474 or target_col == 9474). Every well: [[CDT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
