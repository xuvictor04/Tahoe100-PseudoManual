---
symbol: "NOP16"
type: "gene"
col: 531
ensembl_id: "ENSG00000048162"
name: "NOP16 nucleolar protein"
location: "5q35.2"
module: 5
arm: "+"
pooled_cpm: 10.56
n_lines_expressing: 50
n_dd_up: 47
n_dd_down: 7
n_dd_up_clean: 31
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NOP16

*NOP16 nucleolar protein* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (16 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 3.37× (z +13.3, q 9e-38, up in 43 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.14× (z +8.3, q 2e-14, up in 28 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 0.5 µM: 0.622× (z -5.2, q 9e-05, down in 19 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP2]] (+0.86, fdr 7e-06), [[TWNK]] (+0.84, fdr 7e-06), [[MRTO4]] (+0.83, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 531.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **3.37×** | +13.3 | 9e-38 | 43/47 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.37×** | +9.1 | 2e-17 | 33/39 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +8.3 | 2e-14 | 28/43 (Panc 03.27, HOP62, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.95×** | +7.3 | 3e-11 | 33/47 (SW 900, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.99×** | +7.3 | 4e-11 | 26/41 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.5 | 8e-09 | 26/44 (HS-578T, BT-474, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.80×** | +5.9 | 3e-07 | 24/44 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.77×** | +5.8 | 4e-07 | 26/43 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +5.8 | 4e-07 | 23/47 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.67×** | +5.6 | 9e-07 | 26/44 (NCI-H460, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.40×** | +5.2 | 1e-05 | 21/44 (NCI-H460, HOP62, …) | all doses, flat | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.60×** | +5.2 | 1e-05 | 24/41 (A498, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **2.41×** | +5.1 | 2e-05 | 22/44 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.9 | 4e-05 | 23/45 (SW480, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.8 | 5e-05 | 16/48 (HS-578T, Panc 03.27, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.54×** | +4.6 | 2e-04 | 20/45 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.53×** | +4.5 | 2e-04 | 19/45 (NCI-H1573, NCI-H1792, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +4.4 | 3e-04 | 19/46 (PANC-1, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.33×** | +4.4 | 4e-04 | 11/46 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.78×** | +4.3 | 4e-04 | 15/45 (A498, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 531.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.622×** | -5.2 | 9e-05 | 19/46 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.654×** | -4.7 | 8e-04 | 19/47 (LoVo, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.657×** | -4.5 | 0.001 | 15/45 (LOX-IMVI, HEC-1-A, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.750×** | -4.4 | 0.001 | 20/47 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.671×** | -4.4 | 0.002 | 18/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.761×** | -3.3 | 0.077 | 14/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.772×** | -3.3 | 0.077 | 13/47 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.788× | -3.2 | 0.11 | 12/46 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.753× | -3.1 | 0.11 | 16/47 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.737× | -3.1 | 0.11 | 12/47 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.818× | -3.1 | 0.12 | 8/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 531. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 22.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -14.3) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -8.8) |
| [[A-427 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 6.90 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0599× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.595× (z -8.7) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 5.13 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 10.6× (z +8.7) ⚠ unreliable plate only | — |
| [[PANC-1 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0994× (z -8.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 531), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP2]] | +0.86 | +0.86 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 422 |
| [[TWNK]] | +0.84 | +0.86 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[MRTO4]] | +0.83 | +0.81 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 800 |
| [[PDCD11]] | +0.82 | +0.86 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[BYSL]] | +0.82 | +0.83 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[PUS1]] | +0.82 | +0.86 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[WDR4]] | +0.81 | +0.87 / +0.76 | both halves | 7e-06 |  |
| [[DDX31]] | +0.81 | +0.82 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[DHX33]] | +0.80 | +0.76 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[LYAR]] | +0.80 | +0.82 / +0.80 | both halves | 7e-06 | STRING 407 |
| [[TBRG4]] | +0.78 | +0.75 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[POLR1B]] | +0.77 | +0.77 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises NOP16's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.1% of all compounds | 0.013 | ⚠ off-target possible; 3 compounds |
| [[FUT4]] | B | FUT4 activity lowers NOP16's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 1.35× higher at baseline in the lines without FUT4 | 0.035 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |
| [[ADD3]] | B | ADD3 activity lowers NOP16's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.49× higher at baseline in the lines without ADD3 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[RPP25]] | B | RPP25 activity raises NOP16's level | lines that do not express RPP25 (14) vs lines expressing it (36) | 1.28× lower at baseline in the lines without RPP25 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |
| [[MAP2K2]] | B | MAP2K2 activity raises NOP16's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.831). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.8, -37.5); signed map (-2.1, -47.1). **Vector** length 93.7, 21.9% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.67 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.67 to 19); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.70 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.5 | +13.3 |
|  | [[EX229 (drug)]] 5 µM |  | +4.7 | +5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.2 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +9.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.7 | +5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | +0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.7 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.5 | -4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | NOP16 nucleolar protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:176,383,946-176,388,927 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC111, HSPC185, LOC51491 |
| Hallmark sets | MYC_TARGETS_V2, MYC_TARGETS_V1 |
| Matched by | ensembl_id |

UniProt [Q9Y3C1](https://www.uniprot.org/uniprotkb/Q9Y3C1) carries no function annotation.

**Summary**, from NCBI Gene [51491](https://www.ncbi.nlm.nih.gov/gene/51491):

> This gene encodes a protein that is localized to the nucleolus. Expression of this gene is induced by estrogens and Myc protein and is a marker of poor patient survival in breast cancer. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:26934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26934) · Entrez [51491](https://www.ncbi.nlm.nih.gov/gene/51491) · UniProt [Q9Y3C1](https://www.uniprot.org/uniprotkb/Q9Y3C1) · Ensembl [ENSG00000048162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048162)

## Data

Gene col 531: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 531); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 531, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 531]; `tensor/DDL_lfc|DDL_z.npy` [531]; `embed/gene_vectors.npy` [531]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 531 or target_col == 531). Every well: [[NOP16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOP16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
