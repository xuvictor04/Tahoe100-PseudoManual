---
symbol: "DHRS4L2"
type: "gene"
col: 11931
ensembl_id: "ENSG00000187630"
name: "dehydrogenase/reductase 4 like 2"
location: "14q11.2"
module: 10
arm: "+"
pooled_cpm: 4.43
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# DHRS4L2

*dehydrogenase/reductase 4 like 2* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.09× (z +11.3, q 9e-27, up in 18 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.43× (z +5.1, q 5e-05, up in 9 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.567× (z -5.7, q 7e-06, down in 18 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH5A1]] (+0.64, fdr 1e-05), [[GPLD1]] (+0.63, fdr 1e-05), [[STOX1]] (+0.61, fdr 1e-05); moves opposite to [[RUBCN]] (-0.59, fdr 2e-05), [[PPP1R21]] (-0.59, fdr 4e-05), [[PTPRH]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C10orf95-AS1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11931.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.09×** | +11.3 | 9e-27 | 18/22 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +10.6 | 8e-24 | 6/7 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +7.1 | 3e-10 | 7/11 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +6.9 | 9e-10 | 12/26 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.1 | 5e-05 | 9/43 (NCI-H2347, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.65×** | +5.0 | 6e-05 | 12/42 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.39× | +3.2 | 0.11 | 4/34 (A498, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | 1.25× | +3.2 | 0.11 | 12/37 (HS-578T, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Omeprazole (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.17 | 9/39 (HEC-1-A, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11931.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.567×** | -5.7 | 7e-06 | 18/44 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.577×** | -5.5 | 9e-06 | 19/41 (SW480, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.609×** | -5.0 | 1e-04 | 16/39 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.728×** | -4.5 | 8e-04 | 13/41 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.642×** | -4.5 | 9e-04 | 14/33 (NCI-H23, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.663×** | -4.1 | 0.003 | 12/35 (NCI-H2030, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.708×** | -3.5 | 0.041 | 10/38 (C32, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.706×** | -3.4 | 0.051 | 13/38 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.719×** | -3.3 | 0.056 | 9/42 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.549×** | -3.2 | 0.092 | 7/43 (Panc 03.27, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.809× | -3.0 | 0.13 | 4/44 (SW1417, Hs 766T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11931. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -10.5) |
| [[A-427 (line)]] | wt | 10.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 8.29 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0689× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.656 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11931), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH5A1]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[GPLD1]] | +0.63 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[STOX1]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[CYB5RL]] | +0.61 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[FUBP1]] | +0.61 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[FRG1-DT]] | +0.60 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[FAXC]] | +0.60 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[PRTFDC1]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[DMC1]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[CC2D2A]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SMC1B]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ILF3]] | +0.59 | +0.60 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUBCN]] | -0.59 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R21]] | -0.59 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[PTPRH]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[MAP1LC3B]] | -0.54 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[VRK3]] | -0.53 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[TMEM184B]] | -0.53 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[NIT1]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[SERINC2]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[DUSP18]] | -0.52 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[MTM1]] | -0.51 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[BCLAF3]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[GUK1]] | -0.50 | -0.51 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C10orf95-AS1]] | C | C10orf95-AS1 activity raises DHRS4L2's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 2.05× lower at baseline in the lines without C10orf95-AS1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.456). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.4, 32.4); signed map (31.2, -29.2). **Vector** length 51.6, 7.20% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +5.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +2.7 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -2.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.6 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase/reductase 4 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,969,874-24,006,408 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDR25C3 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PKH6](https://www.uniprot.org/uniprotkb/Q6PKH6) (Dehydrogenase/reductase SDR family member 4-like 2):

> Probable oxidoreductase.

**Summary**, from NCBI Gene [317749](https://www.ncbi.nlm.nih.gov/gene/317749):

> This gene encodes a member of the short chain dehydrogenase reductase family. The encoded protein may be an NADPH dependent retinol oxidoreductase. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:19731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19731) · Entrez [317749](https://www.ncbi.nlm.nih.gov/gene/317749) · UniProt [Q6PKH6](https://www.uniprot.org/uniprotkb/Q6PKH6) · Ensembl [ENSG00000187630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187630)

## Data

Gene col 11931: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11931); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11931, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11931]; `tensor/DDL_lfc|DDL_z.npy` [11931]; `embed/gene_vectors.npy` [11931]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11931 or target_col == 11931). Every well: [[DHRS4L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRS4L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
