---
symbol: "AP5S1"
type: "gene"
col: 4674
ensembl_id: "ENSG00000125843"
name: "adaptor related protein complex 5 subunit sigma 1"
location: "20p13"
module: 95
arm: "+"
pooled_cpm: 4.22
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# AP5S1

*adaptor related protein complex 5 subunit sigma 1* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.21× (z +11.3, q 5e-27, up in 30 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.502× (z -7.0, q 2e-09, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEK8]] (+0.73, fdr 1e-05), [[CREBBP]] (+0.73, fdr 1e-05), [[ZNF689]] (+0.72, fdr 7e-06); moves opposite to [[WASF3]] (-0.68, fdr 5e-05), [[STX7]] (-0.64, fdr 4e-05), [[RNF216P1]] (-0.63, fdr 1e-04).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TNK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4674.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +11.3 | 5e-27 | 30/38 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +5.9 | 1e-06 | 11/48 (NCI-H2030, COLO 205, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.4 | 1e-05 | 2/9 (SNU-423, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +5.0 | 7e-05 | 1/11 (AsPC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.38×** | +4.6 | 4e-04 | 14/37 (NCI-H460, NCI-H2030, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +4.6 | 4e-04 | 10/36 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.4 | 9e-04 | 7/24 (NCI-H2347, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.017 | 9/35 (NCI-H460, HOP62, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.6 | 0.021 | 4/25 (NCI-H460, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.021 | 11/42 (NCI-H2347, LS 180, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.031 | 9/36 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.4 | 0.033 | 1/10 (HOP62) | top dose only | noisy plate (z scaled); position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.099 | 3/44 (NCI-H1792, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4674.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.502×** | -7.0 | 2e-09 | 28/46 (C32, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.512×** | -6.8 | 4e-09 | 26/45 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.306×** | -6.2 | 8e-08 | 23/41 (HS-578T, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.574×** | -5.6 | 3e-06 | 16/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.579×** | -5.5 | 4e-06 | 20/45 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.377×** | -5.2 | 2e-05 | 18/37 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.644×** | -4.4 | 7e-04 | 17/39 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.689×** | -3.6 | 0.022 | 17/38 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.787×** | -3.4 | 0.040 | 13/43 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.719×** | -3.1 | 0.095 | 8/43 (Hs 766T, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 3.32 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0850× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 4.98 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 8.04 | 0 | 1 | — | [[Artemether (drug)]] 0.5 µM 0.0648× (z -8.5) |
| [[SW1417 (line)]] | alt | 3.47 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0738× (z -8.7) |
| [[A-172 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK8]] | +0.73 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[CREBBP]] | +0.73 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[ZNF689]] | +0.72 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ZFX]] | +0.72 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[BOLA1]] | +0.71 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[INO80D]] | +0.71 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[LANCL2]] | +0.71 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ARMC5]] | +0.71 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[UNK]] | +0.70 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[LINC02307]] | +0.69 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[ZBED5]] | +0.69 | +0.68 / +0.39 | both halves | 5e-05 |  |
| [[SPART-AS1]] | +0.69 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.68 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[STX7]] | -0.64 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[RNF216P1]] | -0.63 | -0.69 / -0.34 | both halves | 1e-04 |  |
| [[NBPF3]] | -0.63 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[ANKRD27]] | -0.62 | -0.63 / -0.21 | both halves | 6e-04 |  |
| [[ACTR5]] | -0.61 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[PAPSS1]] | -0.60 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[PCMT1]] | -0.60 | -0.57 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNK1]] | B | TNK1 activity raises AP5S1's level | lines that do not express TNK1 (13) vs lines expressing it (37) | 1.20× lower at baseline in the lines without TNK1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TUBA4A, CDCP1, CHMP4C; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises AP5S1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.787). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (2.2, 9.7); signed map (21.3, -17.4). **Vector** length 58.3, 8.36% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chromatin organization* (reactome, mean cos +0.58 to 7); *Activation of HOX genes during differentiation* (reactome, mean cos +0.61 to 4); *Activation of anterior HOX genes in hindbrain development during early embryogenesis* (reactome, mean cos +0.61 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.9 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.6 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | -5.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -4.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 5 subunit sigma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,820,524-3,828,838 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11168; previously C20orf29 |
| Gene groups (HGNC) | Adaptor related protein complex 5 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUS5](https://www.uniprot.org/uniprotkb/Q9NUS5) (AP-5 complex subunit sigma-1):

> As part of AP-5, a probable fifth adaptor protein complex it may be involved in endosomal transport. According to PubMed:20613862, it is required for efficient homologous recombination DNA double-strand break repair.

**Summary**, from NCBI Gene [55317](https://www.ncbi.nlm.nih.gov/gene/55317):

> Involved in double-strand break repair via homologous recombination and endosomal transport. Located in cytosol; late endosome; and lysosome. Part of AP-type membrane coat adaptor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15875](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15875) · Entrez [55317](https://www.ncbi.nlm.nih.gov/gene/55317) · UniProt [Q9NUS5](https://www.uniprot.org/uniprotkb/Q9NUS5) · Ensembl [ENSG00000125843](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125843)

## Data

Gene col 4674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4674); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4674]; `tensor/DDL_lfc|DDL_z.npy` [4674]; `embed/gene_vectors.npy` [4674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4674 or target_col == 4674). Every well: [[AP5S1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP5S1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
