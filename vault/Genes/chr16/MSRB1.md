---
symbol: "MSRB1"
type: "gene"
col: 12661
ensembl_id: "ENSG00000198736"
name: "methionine sulfoxide reductase B1"
location: "16p13.3"
module: 7
arm: "+"
pooled_cpm: 3.69
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MSRB1

*methionine sulfoxide reductase B1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.81× (z +11.7, q 1e-28, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.381× (z -7.1, q 5e-10, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJB1]] (+0.66, fdr 1e-05), [[ISCA2]] (+0.61, fdr 2e-05), [[COA3]] (+0.59, fdr 1e-05); moves opposite to [[KLHL23]] (-0.55, fdr 3e-04), [[CTTN-DT]] (-0.52, fdr 2e-04), [[TMA7]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.81×** | +11.7 | 1e-28 | 40/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.61×** | +9.5 | 4e-19 | 42/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.37×** | +9.0 | 3e-17 | 37/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.71×** | +7.4 | 2e-11 | 32/43 (HOP62, SW480, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.22×** | +5.7 | 1e-06 | 2/7 (A498, NCI-H2347) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.93×** | +4.9 | 1e-04 | 18/37 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.57×** | +4.7 | 2e-04 | 10/32 (KATO III, HT-29, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +4.6 | 3e-04 | 16/40 (COLO 205, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.91×** | +4.6 | 3e-04 | 15/40 (KATO III, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.83×** | +4.5 | 4e-04 | 22/42 (HOP62, HT-29, …) | two highest doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +4.1 | 0.002 | 10/44 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Larotrectinib (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.009 | 7/44 (PANC-1, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.63×** | +3.6 | 0.012 | 3/18 (A498, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.071 | 9/31 (J82, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +3.1 | 0.085 | 6/19 (LS 180, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12661.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.381×** | -7.1 | 5e-10 | 31/46 (COLO 205, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.501×** | -5.1 | 9e-05 | 22/42 (HT-29, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.530×** | -4.7 | 5e-04 | 25/43 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.379×** | -3.8 | 0.024 | 16/38 (COLO 205, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.384×** | -3.7 | 0.024 | 12/32 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.628×** | -3.4 | 0.056 | 17/33 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0246× (z -14.2) |
| [[HT-29 (line)]] | alt | 4.24 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0716× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 6.49 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.06 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0698× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.976 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB1]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ISCA2]] | +0.61 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[COA3]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CYB5R1]] | +0.59 | +0.55 / +0.35 | both halves | 1e-04 |  |
| [[TM2D2]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CDK5]] | +0.58 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[PSMD3]] | +0.57 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[RPUSD1]] | +0.56 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[THAP7]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[DOLPP1]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[POP4]] | +0.55 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[UBC]] | +0.55 | +0.41 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL23]] | -0.55 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[CTTN-DT]] | -0.52 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[TMA7]] | -0.51 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[UGDH-AS1]] | -0.50 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[MSTO1]] | -0.50 | -0.03 / -0.55 | ⚠ one half (not replicated) | 0.006 |  |
| [[BICRAL]] | -0.48 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[LINC00938]] | -0.48 | -0.26 / -0.38 | both halves | 3e-04 |  |
| [[TRIM66]] | -0.48 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[SLC12A2-DT]] | -0.48 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[CYP4V2]] | -0.48 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[ARGLU1]] | -0.48 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[SDHAF4]] | -0.48 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[PHOSPHO2]] | -0.48 | -0.30 / -0.56 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.310). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-43.3, -6.0); signed map (-18.7, -8.2). **Vector** length 63.5, 10.8% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.1 | +4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.6 | +9.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +11.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | -0.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.6 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +4.6 |
|  | [[Thymol (drug)]] 5 µM |  | +1.3 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.5 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -0.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.5 | -0.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | methionine sulfoxide reductase B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,938,229-1,943,199 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SelR, SepR, SelX, SELENOX, SELENOR; previously SEPX1 |
| Gene groups (HGNC) | Selenoproteins; Methionine sulfoxide reductases |
| Hallmark sets | COMPLEMENT |
| Reactome | 1 pathways, smallest: Protein repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZV6](https://www.uniprot.org/uniprotkb/Q9NZV6) (Methionine-R-sulfoxide reductase B1):

> Methionine-sulfoxide reductase that specifically reduces methionine (R)-sulfoxide back to methionine. While in many cases, methionine oxidation is the result of random oxidation following oxidative stress, methionine oxidation is also a post-translational modification that takes place on specific residue. Acts as a regulator of actin assembly by reducing methionine (R)-sulfoxide mediated by MICALs (MICAL1, MICAL2 or MICAL3) on actin, thereby promoting filament repolymerization. Plays a role in …

**Summary**, from NCBI Gene [51734](https://www.ncbi.nlm.nih.gov/gene/51734):

> The protein encoded by this gene belongs to the methionine-R-sulfoxide reductase B (MsrB) family. Members of this family function as repair enzymes that protect proteins from oxidative stress by catalyzing the reduction of methionine-R-sulfoxides to methionines. This protein is highly expressed in liver and kidney, and is localized to the nucleus and cytosol. It is the only member of the MsrB family that is a selenoprotein, containing a selenocysteine (Sec) residue at its active site. It also …

**Accessions** — [HGNC:14133](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14133) · Entrez [51734](https://www.ncbi.nlm.nih.gov/gene/51734) · UniProt [Q9NZV6](https://www.uniprot.org/uniprotkb/Q9NZV6) · Ensembl [ENSG00000198736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198736)

## Data

Gene col 12661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12661); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12661]; `tensor/DDL_lfc|DDL_z.npy` [12661]; `embed/gene_vectors.npy` [12661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12661 or target_col == 12661). Every well: [[MSRB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSRB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
