---
symbol: "CENPW"
type: "gene"
col: 12785
ensembl_id: "ENSG00000203760"
name: "centromere protein W"
location: "6q22.32"
module: 67
arm: "+"
pooled_cpm: 9.49
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CENPW

*centromere protein W* — 6q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.35× (z +9.2, q 3e-17, up in 40 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.76× (z +3.1, q 0.081, up in 15 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 5.06×, NCI-H460 7.03×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0392×); [[Bortezomib (drug)]] 0.05 µM in 1 line (LS 180 0.0276×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.128×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (C-33 A 0.0497×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT1]] (+0.78, fdr 7e-06), [[UBE2T]] (+0.75, fdr 7e-06), [[GMNN]] (+0.72, fdr 1e-05); moves opposite to [[RNF6]] (-0.59, fdr 5e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PBK]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 15 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12785.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 5.06×, NCI-H460 7.03×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.35×** | +9.2 | 3e-17 | 40/44 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **2.69×** | +7.5 | 2e-11 | 39/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **2.02×** | +5.3 | 2e-05 | 27/39 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.94×** | +5.0 | 7e-05 | 28/47 (NCI-H23, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.89×** | +4.9 | 1e-04 | 27/47 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +4.7 | 3e-04 | 24/38 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.83×** | +4.6 | 3e-04 | 29/47 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.80×** | +4.5 | 5e-04 | 26/47 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.78×** | +4.4 | 8e-04 | 21/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~74% of this change | **1.77×** | +4.2 | 0.002 | 21/39 (A-427, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.62×** | +3.7 | 0.012 | 19/34 (PANC-1, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.67×** | +3.6 | 0.014 | 13/25 (PANC-1, HT-29, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.52×** | +3.2 | 0.059 | 18/45 (NCI-H23, A-427, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +3.1 | 0.069 | 18/48 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.76×** | +3.1 | 0.081 | 15/44 (HOP62, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12785.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0392×); [[Bortezomib (drug)]] 0.05 µM in 1 line (LS 180 0.0276×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.128×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (C-33 A 0.0497×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.716× | -3.4 | 0.26 | 16/48 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.654× | -3.2 | 0.26 | 18/43 (Panc 03.27, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.641× | -3.1 | 0.26 | 7/47 (A549, A-172, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.665× | -3.1 | 0.26 | 12/48 (NCI-H1792, A498, …) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.667× | -3.0 | 0.26 | 20/46 (LoVo, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, +0.73 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 8.48 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0497× (z -9.6) |
| [[LS 180 (line)]] | wt | 8.70 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0276× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 5.82 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 7.03× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[Panc 03.27 (line)]] | alt | 9.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0392× (z -12.6) |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.06× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A-172 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT1]] | +0.78 | +0.78 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[UBE2T]] | +0.75 | +0.68 / +0.72 | both halves | 7e-06 | STRING 667 |
| [[GMNN]] | +0.72 | +0.57 / +0.70 | both halves | 1e-05 | STRING 632 |
| [[STIL]] | +0.71 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[MIS18BP1]] | +0.71 | +0.67 / +0.62 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 728 |
| [[RBL1]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ZDHHC12]] | +0.70 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SPC24]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 | STRING 761 |
| [[HMGB1P5]] ⚠ | +0.70 | +0.60 / +0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPA3]] | +0.69 | +0.64 / +0.65 | both halves | 7e-06 | pathway: Chromosome Maintenance |
| [[ANAPC11]] | +0.68 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CEP152]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[RTTN]] | +0.66 | +0.63 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF6]] | -0.59 | -0.56 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBK]] | C | PBK activity raises CENPW's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.85× lower at baseline in the lines without PBK | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[DIAPH3]], [[MELK]] | C | DIAPH3, MELK activity raises CENPW's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 1.85× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[AURKB]] | C | AURKB activity raises CENPW's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without AURKB | 0.077 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises CENPW's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 1.62× lower at baseline in the lines without CDCA3 | 0.090 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-32.1, -51.6); signed map (-43.8, -39.0). **Vector** length 75.5, 17.2% of its response variance represented; |z| ≥ 3 in 763 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.62 to 12); *G2/M checkpoint* (hallmark, mean cos +0.59 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.59 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +3.8 | +9.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +3.3 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +3.1 | +4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +2.7 | +4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +2.7 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -3.4 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein W |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.32 — chr6:126,340,115-126,348,875 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CUG2; previously C6orf173 |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 4 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Chromosome Maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5EE01](https://www.uniprot.org/uniprotkb/Q5EE01) (Centromere protein W):

> Component of the CENPA-NAC (nucleosome-associated) complex, a complex that plays a central role in assembly of kinetochore proteins, mitotic progression and chromosome segregation (By similarity). The CENPA-NAC complex recruits the CENPA-CAD (nucleosome distal) complex and may be involved in incorporation of newly synthesized CENPA into centromeres (By similarity). Part of a nucleosome-associated complex that binds specifically to histone H3-containing nucleosomes at the centromere, as opposed …

**Summary**, from NCBI Gene [387103](https://www.ncbi.nlm.nih.gov/gene/387103):

> Predicted to enable DNA binding activity and protein heterodimerization activity. Involved in chromosome segregation; kinetochore assembly; and mitotic cell cycle. Located in kinetochore and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21488) · Entrez [387103](https://www.ncbi.nlm.nih.gov/gene/387103) · UniProt [Q5EE01](https://www.uniprot.org/uniprotkb/Q5EE01) · Ensembl [ENSG00000203760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203760)

## Data

Gene col 12785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12785); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12785]; `tensor/DDL_lfc|DDL_z.npy` [12785]; `embed/gene_vectors.npy` [12785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12785 or target_col == 12785). Every well: [[CENPW — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPW.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
