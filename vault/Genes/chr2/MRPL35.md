---
symbol: "MRPL35"
type: "gene"
col: 5296
ensembl_id: "ENSG00000132313"
name: "mitochondrial ribosomal protein L35"
location: "2p11.2"
module: 16
arm: "+"
pooled_cpm: 13.33
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# MRPL35

*mitochondrial ribosomal protein L35* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.03× (z +9.9, q 2e-20, up in 42 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (COLO 205 0.0836×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERAL1]] (+0.71, fdr 7e-06), [[NOL11]] (+0.63, fdr 7e-06), [[PPIL1]] (+0.61, fdr 8e-06); moves opposite to [[TPT1]] (-0.62, fdr 1e-05), [[LRRC75A]] (-0.56, fdr 3e-05), [[RPLP2]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +9.9 | 2e-20 | 42/46 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.99×** | +9.3 | 3e-18 | 37/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.85×** | +8.7 | 8e-16 | 27/36 (A-172, MIA PaCa-2, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.76×** | +7.9 | 4e-13 | 37/47 (A498, A549, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.65×** | +7.1 | 2e-10 | 34/48 (A498, A549, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +6.5 | 7e-09 | 25/41 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +6.5 | 8e-09 | 31/47 (LOX-IMVI, PANC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +6.4 | 1e-08 | 26/48 (HOP62, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.37×** | +6.3 | 2e-08 | 24/46 (A498, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.3 | 2e-08 | 26/46 (A498, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.54×** | +6.0 | 9e-08 | 24/47 (A498, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.0 | 1e-07 | 22/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.56×** | +5.8 | 3e-07 | 24/44 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.49×** | +5.6 | 7e-07 | 24/42 (AsPC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.46×** | +4.9 | 3e-05 | 14/31 (RPMI-7951, HT-29, …) | all doses, flat | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.010 | 14/47 (SW480, SNU-423, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.62×** | +3.6 | 0.010 | 7/45 (PANC-1, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.016 | 9/47 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +3.3 | 0.025 | 9/44 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.025 | 2/46 (NCI-H460, SK-MEL-2) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 1.17× | +3.1 | 0.042 | 12/48 (PANC-1, NCI-H2030, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.49×** | +2.9 | 0.071 | 2/45 (Hs 766T, NCI-H460) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5296.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (COLO 205 0.0836×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.860× | -3.1 | 0.66 | 8/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM |  | 0.801× | -3.0 | 0.66 | 6/46 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | — |
| [[COLO 205 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0836× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERAL1]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 | pathway: Mitochondrial ribosome-associated quality control |
| [[NOL11]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[PTCD2]] | +0.61 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[FUNDC1]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[HGH1]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[DCLRE1A]] | +0.59 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CHD8]] | +0.59 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[DDX20]] | +0.59 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[C9orf64]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[BBS10]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPT1]] | -0.62 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[LRRC75A]] | -0.56 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[RPLP2]] | -0.54 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[PHF1]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[EEF1D]] | -0.53 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[RPL21]] ⚠ | -0.53 | -0.51 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ADIPOR1]] | -0.52 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[RPS6KA5]] | -0.52 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[STAG3L4-1]] | -0.52 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[CCDC65]] | -0.52 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[RPLP1]] | -0.51 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[KDELR1]] | -0.51 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[RPS12]] | -0.51 | -0.53 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MRPL35's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.558). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.7, 13.3); signed map (2.8, -35.9). **Vector** length 56.2, 8.59% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +9.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.1 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +6.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +3.2 |
| fall | [[Temsirolimus (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:86,199,355-86,213,790 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bL35m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9NZE8](https://www.uniprot.org/uniprotkb/Q9NZE8) carries no function annotation.

**Summary**, from NCBI Gene [51318](https://www.ncbi.nlm.nih.gov/gene/51318):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14489](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14489) · Entrez [51318](https://www.ncbi.nlm.nih.gov/gene/51318) · UniProt [Q9NZE8](https://www.uniprot.org/uniprotkb/Q9NZE8) · Ensembl [ENSG00000132313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132313)

## Data

Gene col 5296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5296); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5296]; `tensor/DDL_lfc|DDL_z.npy` [5296]; `embed/gene_vectors.npy` [5296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5296 or target_col == 5296). Every well: [[MRPL35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
