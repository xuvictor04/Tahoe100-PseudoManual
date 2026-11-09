---
symbol: "ZCCHC4"
type: "gene"
col: 9613
ensembl_id: "ENSG00000168228"
name: "zinc finger CCHC-type containing 4"
location: "4p15.2"
module: 20
arm: "+"
pooled_cpm: 21.28
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ZCCHC4

*zinc finger CCHC-type containing 4* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.51× (z +6.1, q 6e-07, up in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.48× (z +5.9, q 9e-07, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.699× (z -5.4, q 4e-05, down in 23 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 0.597× (z -4.0, q 0.010, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCC1]] (+0.66, fdr 7e-06), [[RCC1L]] (+0.62, fdr 1e-05), [[PPWD1]] (+0.61, fdr 1e-05); moves opposite to [[KLF2]] (-0.68, fdr 3e-05), [[JUND]] (-0.60, fdr 5e-05), [[MIDN]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9613.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +6.1 | 6e-07 | 33/47 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +5.9 | 9e-07 | 23/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +5.9 | 9e-07 | 27/47 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +5.6 | 3e-06 | 28/48 (KATO III, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 0.001 | 24/48 (HOP62, SW 900, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.004 | 21/48 (A-172, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.21×** | +4.0 | 0.005 | 18/48 (KATO III, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.8 | 0.011 | 1/48 (CHP-212) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.27×** | +3.6 | 0.020 | 14/48 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.022 | 17/47 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.024 | 14/47 (KATO III, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.054 | 16/48 (RKO, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9613.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.699×** | -5.4 | 4e-05 | 23/44 (A-427, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -5.1 | 1e-04 | 26/45 (J82, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.597×** | -4.0 | 0.010 | 23/45 (AsPC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.725×** | -3.4 | 0.080 | 12/47 (Hs 766T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.732×** | -3.4 | 0.090 | 17/46 (RPMI-7951, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.754× | -3.0 | 0.23 | 17/47 (Hs 766T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 33.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -12.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.116× (z -10.3) |
| [[C-33 A (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0890× (z -10.3) ⚠ toxic |
| [[C32 (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -11.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.0805× (z -8.6) |
| [[HCT15 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.194× (z -9.1) |
| [[HT-29 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +8.5) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[J82 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.238× (z -10.4) ⚠ toxic |
| [[KATO III (line)]] | alt | 18.0 | 0 | 1 | — | [[Pimitespib (drug)]] 5 µM 0.0612× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.136× (z -8.9) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCC1]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[RCC1L]] | +0.62 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PPWD1]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[GPALPP1]] | +0.61 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[STX16]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[EIF2D]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[METTL3]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 | same gene group; STRING 821 |
| [[PAAF1]] | +0.60 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[BABAM1]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[RFT1]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[NAXD]] | +0.58 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[CDC23]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF2]] | -0.68 | -0.46 / -0.71 | both halves | 3e-05 |  |
| [[JUND]] | -0.60 | -0.40 / -0.69 | both halves | 5e-05 |  |
| [[MIDN]] | -0.57 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[HDAC5]] | -0.56 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[C11orf96]] | -0.56 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[UGCG]] | -0.54 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[NR4A1]] | -0.54 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[CBX4]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[RHOB]] | -0.53 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[CDKN2D]] | -0.53 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[PPP1R13B]] | -0.52 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[BBC3]] | -0.52 | -0.43 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.390). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-9.6, 18.2); signed map (-18.6, -31.9). **Vector** length 72.1, 12.3% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +3.9 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.6 | +6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +1.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.4 | -5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | +1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCHC-type containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:25,312,774-25,370,383 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC052, FLJ23024, ZGRF4 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; Zinc fingers GRF-type; 7BS N6-adenosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5U6](https://www.uniprot.org/uniprotkb/Q9H5U6) (rRNA N(6)-adenosine-methyltransferase ZCCHC4):

> rRNA N6-methyltransferase that specifically methylates the adenine in position 4220 of 28S rRNA. N6-methylation of adenine(4220) in 28S rRNA is required for translation.

**Summary**, from NCBI Gene [29063](https://www.ncbi.nlm.nih.gov/gene/29063):

> Enables S-adenosyl-L-methionine binding activity; rRNA (adenine-N6-)-methyltransferase activity; and zinc ion binding activity. Involved in positive regulation of translation and rRNA methylation. Located in cytoplasm and nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22917](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22917) · Entrez [29063](https://www.ncbi.nlm.nih.gov/gene/29063) · UniProt [Q9H5U6](https://www.uniprot.org/uniprotkb/Q9H5U6) · Ensembl [ENSG00000168228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168228)

## Data

Gene col 9613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9613); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9613]; `tensor/DDL_lfc|DDL_z.npy` [9613]; `embed/gene_vectors.npy` [9613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9613 or target_col == 9613). Every well: [[ZCCHC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCCHC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
