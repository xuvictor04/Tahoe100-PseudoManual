---
symbol: "DDX11"
type: "gene"
col: 278
ensembl_id: "ENSG00000013573"
name: "DEAD/H-box helicase 11"
location: "12p11.21"
module: 6
arm: "+"
pooled_cpm: 21.81
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# DDX11

*DEAD/H-box helicase 11* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (14 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.53× (z +6.8, q 4e-09, up in 25 of 44 measured lines) ⚠ toxic; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.23× (z +3.3, q 0.043, up in 15 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.766× (z -6.4, q 1e-07, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX12P]] (+0.88, fdr 7e-06), [[MCM3]] (+0.85, fdr 7e-06), [[POLA1]] (+0.82, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LRRCC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 16 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 278.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.53×** | +6.8 | 4e-09 | 25/44 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.52×** | +6.5 | 2e-08 | 19/38 (SNU-423, A-427, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.38×** | +5.5 | 9e-06 | 18/47 (SW480, NCI-H2030, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | **1.40×** | +5.4 | 1e-05 | 16/33 (LoVo, CFPAC-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +5.1 | 5e-05 | 19/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.34×** | +5.0 | 6e-05 | 16/47 (PANC-1, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.34×** | +4.9 | 1e-04 | 19/47 (LOX-IMVI, SW48, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.33×** | +4.8 | 1e-04 | 16/47 (SW480, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +4.6 | 2e-04 | 19/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +4.2 | 0.002 | 16/47 (SW480, PANC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +4.0 | 0.004 | 13/47 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.24×** | +3.6 | 0.017 | 14/42 (HT-29, LoVo, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.043 | 15/47 (NCI-H1573, C32, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.2 | 0.053 | 1/48 (RPMI-7951) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.2 | 0.056 | 5/26 (NCI-H2347, HS-578T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 278.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.766×** | -6.4 | 1e-07 | 27/46 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.780×** | -4.0 | 0.011 | 14/47 (LoVo, A-427, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.845× | -4.0 | 0.011 | 20/47 (MIA PaCa-2, SW480, …) | rises with dose | composition shift |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.799×** | -3.8 | 0.020 | 8/48 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.795×** | -3.7 | 0.022 | 17/48 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.806×** | -3.7 | 0.022 | 14/47 (A-172, HCT15, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.861× | -3.6 | 0.022 | 24/48 (A-427, H4, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.744×** | -3.6 | 0.022 | 12/46 (NCI-H23, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.810×** | -3.6 | 0.022 | 12/48 (LoVo, HEC-1-A, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.812×** | -3.5 | 0.024 | 14/48 (SW1417, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.824×** | -3.3 | 0.053 | 16/46 (LS 180, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.830×** | -3.2 | 0.074 | 10/47 (H4, HOP62, …) | two highest doses | low cells (technical?); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 0.837× | -3.1 | 0.074 | 9/48 (A-427, LoVo, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 278. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 41.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -10.7) |
| [[LoVo (line)]] | wt | 31.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -9.3) |
| [[A-427 (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.335× (z -11.6) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A498 (line)]] | wt | 31.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -13.3) |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.123× (z -8.5) |
| [[H4 (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.257× (z -9.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.160× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -14.4) ⚠ cell-cycle shift, explains ~8% of this change |
| [[NCI-H23 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -8.5) ⚠ cell-cycle shift, explains ~8% of this change |
| [[SHP-77 (line)]] | alt | 73.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.6) |
| [[SW48 (line)]] | wt | 24.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -9.9) |
| [[SW480 (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -10.7) ⚠ cell-cycle shift, explains ~8% of this change |
| [[A-172 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 278), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX12P]] | +0.88 | +0.85 / +0.87 | both halves | 7e-06 | same gene group |
| [[MCM3]] | +0.85 | +0.82 / +0.84 | both halves | 7e-06 | STRING 507 |
| [[POLA1]] | +0.82 | +0.79 / +0.82 | both halves | 7e-06 |  |
| [[FANCA]] | +0.81 | +0.79 / +0.79 | both halves | 7e-06 | STRING 632 |
| [[CDCA7]] | +0.80 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[CDC45]] | +0.80 | +0.79 / +0.79 | both halves | 7e-06 | STRING 517 |
| [[POLE2]] | +0.80 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[TONSL]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.79 | +0.75 / +0.78 | both halves | 7e-06 | STRING 813 |
| [[EXO1]] | +0.79 | +0.74 / +0.78 | both halves | 7e-06 | STRING 410 |
| [[MCM2]] | +0.78 | +0.70 / +0.80 | both halves | 7e-06 |  |
| [[MCM5]] | +0.78 | +0.82 / +0.76 | both halves | 7e-06 | STRING 548 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises DDX11's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.29× lower at baseline in the lines without CDC25A | 0.028 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises DDX11's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without CDCA7 | 0.065 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises DDX11's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.66× lower at baseline in the lines without E2F2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises DDX11's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without DSCC1 | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises DDX11's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.39× lower at baseline in the lines without ZNF367 | 0.036 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRCC1]] | C | DDX11's natural level strengthens LRRCC1's drug response | DDX11's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.01; direction clear | 0.061 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.837). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.5, -43.4); signed map (-35.9, -44.5). **Vector** length 106, 24.3% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.63 to 65); *DNA strand elongation* (reactome, mean cos +0.67 to 28); *DNA Replication* (reactome, mean cos +0.66 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | +4.9 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +3.6 | +5.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | +3.2 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.6 | +5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.6 | +4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +1.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.8 | +2.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.4 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -4.2 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.2 | -3.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.4 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -3.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | DEAD/H-box helicase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:31,073,860-31,104,799 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ChlR1, KRG-2, CHL1, WABS |
| Gene groups (HGNC) | DEAD-box helicases; DEAH-box helicases |
| Reactome | 5 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FC9](https://www.uniprot.org/uniprotkb/Q96FC9) (ATP-dependent DNA helicase DDX11):

> DNA-dependent ATPase and ATP-dependent DNA helicase that participates in various functions in genomic stability, including DNA replication, DNA repair and heterochromatin organization as well as in ribosomal RNA synthesis. Its double-stranded DNA helicase activity requires either a minimal 5'-single-stranded tail length of approximately 15 nt (flap substrates) or 10 nt length single-stranded gapped DNA substrates of a partial duplex DNA structure for helicase loading and translocation along DNA …

**Summary**, from NCBI Gene [1663](https://www.ncbi.nlm.nih.gov/gene/1663):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. This gene encodes a …

**Accessions** — [HGNC:2736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2736) · Entrez [1663](https://www.ncbi.nlm.nih.gov/gene/1663) · UniProt [Q96FC9](https://www.uniprot.org/uniprotkb/Q96FC9) · Ensembl [ENSG00000013573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013573)

## Data

Gene col 278: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 278); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 278, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 278]; `tensor/DDL_lfc|DDL_z.npy` [278]; `embed/gene_vectors.npy` [278]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 278 or target_col == 278). Every well: [[DDX11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
