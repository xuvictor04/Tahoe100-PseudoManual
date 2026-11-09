---
symbol: "ZFTA"
type: "gene"
col: 11974
ensembl_id: "ENSG00000188070"
name: "zinc finger translocation associated"
location: "11q13.1"
module: 135
arm: "+"
pooled_cpm: 2.82
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# ZFTA

*zinc finger translocation associated* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.37× (z +8.4, q 2e-14, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +7.7, q 4e-12, up in 18 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Betamethasone dipropionate (drug)]] 5 µM: 0.585× (z -5.3, q 8e-05, down in 18 of 44 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBKBP1]] (+0.61, fdr 4e-05), [[NDRG2]] (+0.60, fdr 1e-05), [[SRC]] (+0.57, fdr 6e-05); moves opposite to [[PARK7]] (-0.60, fdr 2e-05, ⚠ PARK7 in the vector space only through flagged drug-doses), [[PIBF1]] (-0.54, fdr 3e-04), [[CFDP1]] (-0.49, fdr 1e-04), [[KIAA1328]] (-0.49, fdr 6e-04).
> It sits in the **+** arm of [[Module 135]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +8.4 | 2e-14 | 1/3 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.7 | 4e-12 | 18/36 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +7.0 | 6e-10 | 4/16 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +6.8 | 2e-09 | 11/21 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +5.7 | 1e-06 | 19/43 (HOP62, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +5.5 | 4e-06 | 7/45 (C32, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +5.4 | 5e-06 | 7/17 (A-172, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +4.3 | 0.001 | 1/6 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +3.9 | 0.006 | 7/23 (Panc 03.27, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.011 | 7/23 (Hs 766T, J82, …) | two highest doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.032 | 6/29 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.4 | 0.032 | 1/3 (LoVo) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.057 | 2/26 (NCI-H1792, Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.057 | 2/31 (LS 180, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +3.1 | 0.071 | 3/19 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11974.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.585×** | -5.3 | 8e-05 | 18/44 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.645×** | -4.5 | 0.002 | 13/40 (MIA PaCa-2, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.499×** | -3.7 | 0.040 | 11/37 (Hs 766T, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.699×** | -3.6 | 0.051 | 13/46 (HT-29, Panc 03.27, …) | two highest doses | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.719×** | -3.3 | 0.096 | 12/27 (BT-474, HEC-1-A, …) | rises with dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.725×** | -3.3 | 0.096 | 8/46 (HepG2/C3A, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 6.65 | 0 | 2 (1 ⚠) | — | [[Omeprazole (drug)]] 0.5 µM 0.0953× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 3.35 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0986× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 4.17 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0740× (z -8.9) |
| [[A-172 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBKBP1]] | +0.61 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[NDRG2]] | +0.60 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SRC]] | +0.57 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[TNK1]] | +0.57 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[RNF103]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[MGAT4B]] | +0.56 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[TSPYL4]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[INPPL1]] | +0.56 | +0.53 / +0.34 | both halves | 1e-04 |  |
| [[TFAP2A-AS1]] | +0.54 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[MOB3C]] | +0.53 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[RARG]] | +0.53 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[GUCY1A2]] | +0.53 | +0.46 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARK7]] ⚠ | -0.60 | -0.48 / -0.50 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PIBF1]] | -0.54 | -0.58 / -0.29 | both halves | 3e-04 |  |
| [[CFDP1]] | -0.49 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[KIAA1328]] | -0.49 | -0.47 / -0.22 | both halves | 6e-04 |  |
| [[NHP2]] | -0.49 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[EIF3K]] | -0.48 | -0.48 / -0.26 | both halves | 4e-04 |  |
| [[GGCT]] | -0.48 | -0.41 / -0.32 | both halves | 1e-04 |  |
| [[EFHC1]] | -0.47 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[GPN3]] | -0.47 | -0.24 / -0.35 | both halves | 5e-04 |  |
| [[TXNDC17]] | -0.47 | -0.43 / -0.20 | both halves | 7e-04 |  |
| [[NUP58]] | -0.47 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[ATP5MC1]] | -0.47 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[ODF2]] | -0.47 | -0.42 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.493). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (3.9, 33.2); signed map (41.2, -1.6). **Vector** length 44.5, 4.78% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.8 | +5.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +7.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.8 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +8.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.1 | -3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.0 | -2.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.0 | -5.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -0.4 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger translocation associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:63,759,892-63,768,775 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3032; previously C11orf95 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

UniProt [C9JLR9](https://www.uniprot.org/uniprotkb/C9JLR9) carries no function annotation.

**Summary**, from NCBI Gene [65998](https://www.ncbi.nlm.nih.gov/gene/65998):

> Predicted to be involved in negative regulation of DNA-templated transcription. Located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28449) · Entrez [65998](https://www.ncbi.nlm.nih.gov/gene/65998) · UniProt [C9JLR9](https://www.uniprot.org/uniprotkb/C9JLR9) · Ensembl [ENSG00000188070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188070)

## Data

Gene col 11974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11974); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11974]; `tensor/DDL_lfc|DDL_z.npy` [11974]; `embed/gene_vectors.npy` [11974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11974 or target_col == 11974). Every well: [[ZFTA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFTA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
