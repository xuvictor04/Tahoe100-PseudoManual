---
symbol: "ZSCAN9"
type: "gene"
col: 5981
ensembl_id: "ENSG00000137185"
name: "zinc finger and SCAN domain containing 9"
location: "6p22.1"
module: 16
arm: "+"
pooled_cpm: 10.85
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZSCAN9

*zinc finger and SCAN domain containing 9* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.79× (z +12.0, q 1e-30, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.717× (z -6.9, q 3e-09, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF606]] (+0.65, fdr 1e-05), [[TMEM128]] (+0.63, fdr 1e-05), [[ZNF197]] (+0.63, fdr 1e-05); moves opposite to [[COP1]] (-0.56, fdr 2e-05), [[UBE4B]] (-0.54, fdr 1e-05), [[FBXW7]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF571]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +12.0 | 1e-30 | 36/47 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +10.7 | 2e-24 | 36/44 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +6.7 | 3e-09 | 25/46 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +5.5 | 4e-06 | 20/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +5.3 | 1e-05 | 21/47 (NCI-H2030, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.011 | 15/47 (SNU-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.8 | 0.013 | 15/40 (HT-29, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.022 | 9/47 (hTERT-HPNE, SNU-423, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +3.4 | 0.039 | 4/48 (Panc 03.27, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.049 | 9/47 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.059 | 6/44 (RPMI-7951, SNU-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.063 | 9/47 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.2 | 0.063 | 8/47 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.088 | 10/47 (SNU-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.091 | 0/48 | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5981.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -6.9 | 3e-09 | 26/45 (NCI-H2347, SW48, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Arbutin (drug)]] 5 µM |  | **0.769×** | -3.7 | 0.039 | 13/46 (NCI-H2030, SW1417, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.769×** | -3.7 | 0.039 | 16/45 (SNU-423, KATO III, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Trifluridine (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.092 | 11/47 (MIA PaCa-2, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +11.3) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0897× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 2 (1 ⚠) | — | [[Decitabine (drug)]] 0.5 µM 0.0921× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 17.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.139× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 4.24 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0528× (z -10.0) |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0786× (z -10.9) |
| [[HCT15 (line)]] | alt | 9.88 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0848× (z -9.0) |
| [[Hs 766T (line)]] | wt | 5.83 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.0870× (z -9.2) |
| [[HT-29 (line)]] | alt | 7.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 9.14 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW480 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.6) | — |
| [[A-172 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF606]] | +0.65 | +0.58 / +0.56 | both halves | 1e-05 | same gene group |
| [[TMEM128]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[ZNF197]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 | same gene group |
| [[TYW5]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ZNF134]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[ZNF624]] | +0.60 | +0.46 / +0.62 | both halves | 2e-05 | same gene group |
| [[VPS72]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[MRPL58]] | +0.60 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[POLI]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ZNF23]] | +0.59 | +0.63 / +0.50 | both halves | 1e-05 | same gene group |
| [[PYM1]] | +0.59 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[MIOS]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COP1]] | -0.56 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[UBE4B]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[FBXW7]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[TNPO3]] | -0.54 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[TTLL5]] | -0.52 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[MBOAT7]] | -0.52 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[SNTB2]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[GLG1]] | -0.51 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[BCO2]] | -0.50 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[BIRC6]] | -0.50 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[SBNO1]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[PCYOX1]] | -0.50 | -0.36 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF571]] | B | ZNF571 activity raises ZSCAN9's level | lines that do not express ZNF571 (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without ZNF571 | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.1, 6.6); signed map (3.8, -25.5). **Vector** length 58.4, 7.75% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.0 | +1.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -0.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:28,224,886-28,233,487 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRD51; previously ZNF193 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O15535](https://www.uniprot.org/uniprotkb/O15535) (Zinc finger and SCAN domain-containing protein 9):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7746](https://www.ncbi.nlm.nih.gov/gene/7746):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12984) · Entrez [7746](https://www.ncbi.nlm.nih.gov/gene/7746) · UniProt [O15535](https://www.uniprot.org/uniprotkb/O15535) · Ensembl [ENSG00000137185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137185)

## Data

Gene col 5981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5981); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5981]; `tensor/DDL_lfc|DDL_z.npy` [5981]; `embed/gene_vectors.npy` [5981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5981 or target_col == 5981). Every well: [[ZSCAN9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
