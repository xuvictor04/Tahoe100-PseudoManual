---
symbol: "RPL18A"
type: "gene"
col: 2632
ensembl_id: "ENSG00000105640"
name: "ribosomal protein L18a"
location: "19p13.11"
module: 20
arm: "+"
pooled_cpm: 11.57
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RPL18A

*ribosomal protein L18a* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.23× (z +9.7, q 1e-19, up in 31 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 5.47× (z +7.4, q 2e-11, up in 42 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.223×); [[Rimonabant (drug)]] 0.5 µM in 1 line (HCT15 0.0763×); [[Thymol (drug)]] 0.5 µM in 1 line (Hs 766T 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL10]] (+0.85, fdr 7e-06), [[RPS18]] (+0.82, fdr 7e-06), [[ANKRD30BL]] (+0.78, fdr 7e-06); moves opposite to [[CROCCP2-1]] (-0.56, fdr 1e-05), [[RBX1]] (-0.53, fdr 1e-05), [[PIGBOS1]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRTAP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2632.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.23×** | +9.7 | 1e-19 | 31/35 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.39×** | +9.3 | 3e-18 | 40/48 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +8.1 | 9e-14 | 25/27 (LoVo, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **5.47×** | +7.4 | 2e-11 | 42/47 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.93×** | +6.4 | 2e-08 | 40/45 (NCI-H460, LoVo, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +6.2 | 5e-08 | 18/22 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **2.08×** | +6.1 | 1e-07 | 34/47 (LoVo, SW480, …) | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 0.05 µM |  | **2.17×** | +5.9 | 2e-07 | 37/46 (LoVo, SW480, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.73×** | +5.7 | 7e-07 | 29/44 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 5 µM |  | **2.81×** | +4.5 | 4e-04 | 25/36 (NCI-H460, LOX-IMVI, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +4.2 | 0.001 | 22/47 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.7 | 0.011 | 21/41 (LoVo, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **1.55×** | +3.6 | 0.015 | 17/48 (LoVo, LS 180, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 0.05 µM |  | **1.59×** | +3.5 | 0.017 | 17/46 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +3.5 | 0.017 | 17/42 (SW 900, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.062 | 14/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.68×** | +3.0 | 0.069 | 11/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2632.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.223×); [[Rimonabant (drug)]] 0.5 µM in 1 line (HCT15 0.0763×); [[Thymol (drug)]] 0.5 µM in 1 line (Hs 766T 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.652× | -3.6 | 0.11 | 18/47 (RPMI-7951, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.659× | -3.5 | 0.11 | 19/47 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Trimetrexate (drug)]] 0.05 µM |  | 0.667× | -3.4 | 0.11 | 18/46 (HCT15, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Glasdegib (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.691× | -3.1 | 0.25 | 4/47 (NCI-H2030, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.689× | -3.0 | 0.27 | 14/46 (KATO III, C-33 A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 2 | — | [[Thymol (drug)]] 0.5 µM 0.109× (z -8.9) |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 1 | — | [[Rimonabant (drug)]] 0.5 µM 0.0763× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 1 | — | [[Auranofin (drug)]] 0.05 µM 0.0871× (z -8.5) |
| [[RKO (line)]] | wt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -9.1) |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.106× (z -8.5) |
| [[A-172 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL10]] | +0.85 | +0.76 / +0.83 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS18]] | +0.82 | +0.77 / +0.79 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[ANKRD30BL]] | +0.78 | +0.75 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RPL3]] | +0.78 | +0.76 / +0.74 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[HFM1]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[RPSA]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3A]] | +0.73 | +0.65 / +0.75 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL29]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL4]] | +0.72 | +0.63 / +0.70 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[EEF1A1]] | +0.71 | +0.73 / +0.70 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 996 |
| [[RPL6]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[EOLA2]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.56 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[RBX1]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 | pathway: Regulation of expression of SLITs and ROBOs |
| [[PIGBOS1]] | -0.53 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[PPP1R12A]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ZNF503]] | -0.53 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[IRX5]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[ERVK3-1]] | -0.51 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[OFD1]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRTAP]] | C | CRTAP activity raises RPL18A's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.42× lower at baseline in the lines without CRTAP | 0.047 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.7, -25.5); signed map (-21.6, -34.4). **Vector** length 74.1, 13.5% of its response variance represented; |z| ≥ 3 in 765 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosomal scanning and start codon recognition* (reactome, mean cos +0.64 to 6); *Translation initiation complex formation* (reactome, mean cos +0.64 to 6); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.64 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +9.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.0 | +3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +1.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +5.7 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.3 | -0.4 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.1 | -3.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.9 | -2.2 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Voriconazole (drug)]] 0.5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L18a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,859,910-17,864,153 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L18A, eL20 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02543](https://www.uniprot.org/uniprotkb/Q02543) (Large ribosomal subunit protein eL20):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6142](https://www.ncbi.nlm.nih.gov/gene/6142):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a member of the L18AE family of ribosomal proteins that is a component of the 60S subunit. The encoded protein may play a role in viral replication by interacting with the hepatitis C virus internal ribosome entry site (IRES). This gene is co-transcribed with …

**Accessions** — [HGNC:10311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10311) · Entrez [6142](https://www.ncbi.nlm.nih.gov/gene/6142) · UniProt [Q02543](https://www.uniprot.org/uniprotkb/Q02543) · Ensembl [ENSG00000105640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105640)

## Data

Gene col 2632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2632); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2632]; `tensor/DDL_lfc|DDL_z.npy` [2632]; `embed/gene_vectors.npy` [2632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2632 or target_col == 2632). Every well: [[RPL18A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL18A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
