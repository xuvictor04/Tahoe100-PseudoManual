---
symbol: "GEMIN6"
type: "gene"
col: 7597
ensembl_id: "ENSG00000152147"
name: "gem nuclear organelle associated protein 6"
location: "2p22.1"
module: 7
arm: "+"
pooled_cpm: 5.64
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# GEMIN6

*gem nuclear organelle associated protein 6* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +6.1, q 4e-07, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.522× (z -6.5, q 3e-08, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRIX1]] (+0.72, fdr 7e-06), [[MRPL46]] (+0.72, fdr 1e-05), [[MRPS26]] (+0.70, fdr 2e-05); moves opposite to [[PRKACA]] (-0.58, fdr 5e-05), [[CHP1]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.1 | 4e-07 | 25/41 (NCI-H1792, SW480, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.88×** | +6.0 | 4e-07 | 4/8 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.80×** | +5.8 | 1e-06 | 20/46 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.76×** | +5.6 | 3e-06 | 21/47 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +5.5 | 4e-06 | 16/46 (A549, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +5.2 | 2e-05 | 14/29 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.65×** | +5.0 | 6e-05 | 8/26 (NCI-H1792, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +4.4 | 6e-04 | 18/46 (NCI-H23, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.4 | 6e-04 | 14/30 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.3 | 0.001 | 19/47 (HOP62, SHP-77, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.54×** | +4.3 | 0.001 | 16/46 (SNU-423, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.8 | 0.007 | 10/44 (PANC-1, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.5 | 0.020 | 3/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.26×** | +3.2 | 0.055 | 8/47 (RPMI-7951, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.36×** | +3.0 | 0.093 | 6/47 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.100 | 4/43 (LoVo, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7597.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.522×** | -6.5 | 3e-08 | 25/45 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.524×** | -6.4 | 3e-08 | 27/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -5.2 | 3e-05 | 24/45 (HCT15, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.759×** | -3.9 | 0.014 | 16/47 (A-427, NCI-H460, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.682×** | -3.8 | 0.015 | 17/40 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.778×** | -3.5 | 0.033 | 16/41 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.507×** | -3.5 | 0.033 | 11/42 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.706×** | -3.5 | 0.036 | 8/46 (NCI-H1792, NCI-H460, …) | top dose only | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.713×** | -3.4 | 0.045 | 16/43 (A-172, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.720×** | -3.3 | 0.060 | 10/45 (A-172, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 7.55 | 0 | 2 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0929× (z -8.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.0945× (z -8.7) |
| [[A-172 (line)]] | wt | 5.28 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0735× (z -9.9) |
| [[A-427 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -8.5) ⚠ cell-cycle shift, explains ~97% of this change |
| [[HT-29 (line)]] | alt | 3.28 | 0 | 1 | — | [[Bexarotene (drug)]] 0.05 µM 0.0490× (z -10.0) |
| [[J82 (line)]] | alt | 3.31 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0702× (z -9.1) |
| [[PANC-1 (line)]] | alt | 7.85 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRIX1]] | +0.72 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[MRPL46]] | +0.72 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[MRPS26]] | +0.70 | +0.49 / +0.76 | both halves | 2e-05 |  |
| [[MRPS12]] | +0.70 | +0.43 / +0.76 | both halves | 3e-05 |  |
| [[MRPS23]] | +0.70 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[RDH14]] | +0.68 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[RPUSD2]] | +0.67 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[MRPL15]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[COA3]] | +0.66 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[COA4]] | +0.66 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[FADD]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[MRPL57]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKACA]] | -0.58 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[CHP1]] | -0.56 | -0.35 / -0.64 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.499). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-44.7, -9.2); signed map (-12.8, -8.3). **Vector** length 46.4, 5.91% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.5 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | -2.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -6.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | +2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.7 | -3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | +0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -3.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.8 | -3.5 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | gem nuclear organelle associated protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.1 — chr2:38,751,534-38,785,002 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23459 |
| Gene groups (HGNC) | Gemins |
| Reactome | 8 pathways, smallest: SARS-CoV-2 modulates host translation machinery; Metabolism of non-coding RNA; snRNP Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXD5](https://www.uniprot.org/uniprotkb/Q8WXD5) (Gem-associated protein 6):

> The SMN complex catalyzes the assembly of small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome, and thereby plays an important role in the splicing of cellular pre-mRNAs. Most spliceosomal snRNPs contain a common set of Sm proteins SNRPB, SNRPD1, SNRPD2, SNRPD3, SNRPE, SNRPF and SNRPG that assemble in a heptameric protein ring on the Sm site of the small nuclear RNA to form the core snRNP (Sm core). In the cytosol, the Sm proteins SNRPD1, SNRPD2, SNRPE, SNRPF and …

**Summary**, from NCBI Gene [79833](https://www.ncbi.nlm.nih.gov/gene/79833):

> GEMIN6 is part of a large macromolecular complex, localized to both the cytoplasm and the nucleus, that plays a role in the cytoplasmic assembly of small nuclear ribonucleoproteins (snRNPs). Other members of this complex include SMN (MIM 600354), GEMIN2 (SIP1; MIM 602595), GEMIN3 (DDX20; MIM 606168), GEMIN4 (MIM 606969), and GEMIN5 (MIM 607005).[supplied by OMIM, Jul 2002]

**Accessions** — [HGNC:20044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20044) · Entrez [79833](https://www.ncbi.nlm.nih.gov/gene/79833) · UniProt [Q8WXD5](https://www.uniprot.org/uniprotkb/Q8WXD5) · Ensembl [ENSG00000152147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152147)

## Data

Gene col 7597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7597); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7597]; `tensor/DDL_lfc|DDL_z.npy` [7597]; `embed/gene_vectors.npy` [7597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7597 or target_col == 7597). Every well: [[GEMIN6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GEMIN6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
