---
symbol: "RFC5"
type: "gene"
col: 3233
ensembl_id: "ENSG00000111445"
name: "replication factor C subunit 5"
location: "12q24.23"
module: 6
arm: "+"
pooled_cpm: 19.56
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RFC5

*replication factor C subunit 5* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.21× (z +13.1, q 3e-36, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.36× (z +5.1, q 2e-05, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.803× (z -5.1, q 2e-04, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRM1]] (+0.86, fdr 7e-06), [[EXO1]] (+0.86, fdr 7e-06), [[WDR76]] (+0.84, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDCA7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 20 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **2.21×** | +13.1 | 3e-36 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **2.18×** | +12.8 | 4e-35 | 36/42 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **2.10×** | +12.2 | 4e-32 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.85×** | +10.1 | 7e-22 | 40/47 (LoVo, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **1.84×** | +9.6 | 6e-20 | 24/30 (A549, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **1.59×** | +7.0 | 2e-10 | 23/37 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.45×** | +6.1 | 8e-08 | 21/47 (J82, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~82% of this change | **1.45×** | +5.9 | 3e-07 | 20/43 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.2 | 1e-05 | 1/48 (NCI-H2030) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +5.1 | 2e-05 | 19/47 (HOP62, SW480, …) | two highest doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.23×** | +4.8 | 7e-05 | 15/48 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.31×** | +4.5 | 3e-04 | 22/47 (HepG2/C3A, HOP62, …) | two highest doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.30×** | +4.4 | 6e-04 | 18/48 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.0 | 0.003 | 18/47 (A498, LoVo, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.006 | 15/47 (LS 180, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.013 | 10/45 (A498, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.20×** | +3.0 | 0.063 | 8/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.078 | 7/45 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.803×** | -5.1 | 2e-04 | 23/47 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.776×** | -4.2 | 0.008 | 16/46 (C-33 A, SK-MEL-2, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.788×** | -3.9 | 0.012 | 17/45 (H4, LoVo, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.846× | -3.9 | 0.012 | 15/48 (A-427, PANC-1, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.730×** | -3.7 | 0.023 | 14/48 (A498, A-172, …) | two highest doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.863× | -3.4 | 0.055 | 13/48 (RPMI-7951, RKO, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.814×** | -3.4 | 0.055 | 21/47 (A-427, SNU-1, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | 0.700× | -3.1 | 0.15 | 10/45 (NCI-H2030, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | 0.836× | -3.0 | 0.15 | 7/48 (A-427, SNU-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.92 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 16.5 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.94× (z +9.3) ⚠ cell-cycle shift, explains ~83% of this change | — |
| [[SW480 (line)]] | alt | 30.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +8.8) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[A-427 (line)]] | wt | 33.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.311× (z -9.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A549 (line)]] | wt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.40× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | — |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.0) |
| [[H4 (line)]] | wt | 13.9 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.212× (z -9.4) |
| [[HCT15 (line)]] | alt | 35.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -9.8) |
| [[Hs 766T (line)]] | wt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.79× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | — |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.376× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 31.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.7) |
| [[SW48 (line)]] | wt | 28.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.151× (z -9.0) |
| [[A-172 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRM1]] | +0.86 | +0.87 / +0.83 | both halves | 7e-06 | STRING 650 |
| [[EXO1]] | +0.86 | +0.87 / +0.84 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 825 |
| [[WDR76]] | +0.84 | +0.83 / +0.83 | both halves | 7e-06 |  |
| [[CDC45]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 728 |
| [[ORC1]] | +0.83 | +0.84 / +0.81 | both halves | 7e-06 | same gene group; pathway: Activation of ATR in response to replication stress; STRING 491 |
| [[CENPK]] | +0.83 | +0.79 / +0.83 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[MYBL2]] | +0.83 | +0.83 / +0.83 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.83 | +0.79 / +0.82 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 999 |
| [[FANCI]] | +0.82 | +0.81 / +0.80 | both halves | 7e-06 | STRING 529 |
| [[POLQ]] | +0.81 | +0.82 / +0.80 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[DTL]] | +0.81 | +0.85 / +0.79 | both halves | 7e-06 | pathway: DNA Damage Bypass; STRING 671 |
| [[WDHD1]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 | STRING 695 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7]] | B | CDCA7 activity raises RFC5's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without CDCA7 | 0.077 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises RFC5's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without E2F8 | 0.087 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.870). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.7, -44.8); signed map (-37.6, -43.3). **Vector** length 106, 25.9% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.66 to 65); *E2F G1/S* (control, mean cos +0.68 to 23); *Activation of the pre-replicative complex* (reactome, mean cos +0.72 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +3.9 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +3.8 | +12.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +3.8 | +10.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +3.8 | +13.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +3.6 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +5.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +2.4 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.1 | +1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -5.1 | -3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.2 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.8 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | replication factor C subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:118,013,588-118,033,130 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RFC36 |
| Gene groups (HGNC) | AAA ATPases; Replication factor C |
| Hallmark sets | DNA_REPAIR |
| Reactome | 59 pathways, smallest: Leading Strand Synthesis; Polymerase switching; Translesion synthesis by REV1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P40937](https://www.uniprot.org/uniprotkb/P40937) (Replication factor C subunit 5):

> Subunit of the replication factor C (RFC) complex which acts during elongation of primed DNA templates by DNA polymerases delta and epsilon, and is necessary for ATP-dependent loading of proliferating cell nuclear antigen (PCNA) onto primed DNA.

**Summary**, from NCBI Gene [5985](https://www.ncbi.nlm.nih.gov/gene/5985):

> This gene encodes the smallest subunit of the replication factor C complex, which consists of five distinct subunits (140, 40, 38, 37, and 36 kDa) and is required for DNA replication. This subunit interacts with the C-terminal region of proliferating cell nuclear antigen and is required to open and load proliferating cell nuclear antigen onto DNA during S phase. It is a member of the AAA+ (ATPases associated with various cellular activities) ATPase family and forms a core complex with the 38 …

**Accessions** — [HGNC:9973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9973) · Entrez [5985](https://www.ncbi.nlm.nih.gov/gene/5985) · UniProt [P40937](https://www.uniprot.org/uniprotkb/P40937) · Ensembl [ENSG00000111445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111445)

## Data

Gene col 3233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3233); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3233]; `tensor/DDL_lfc|DDL_z.npy` [3233]; `embed/gene_vectors.npy` [3233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3233 or target_col == 3233). Every well: [[RFC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
