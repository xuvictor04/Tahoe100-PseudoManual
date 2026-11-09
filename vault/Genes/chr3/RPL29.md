---
symbol: "RPL29"
type: "gene"
col: 8495
ensembl_id: "ENSG00000162244"
name: "ribosomal protein L29"
location: "3p21.2"
module: 43
arm: "+"
pooled_cpm: 34.16
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL29

*ribosomal protein L29* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.73× (z +9.5, q 2e-18, up in 35 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +4.2, q 0.003, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.464× (z -9.8, q 7e-20, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EEF1G]] (+0.87, fdr 7e-06), [[RPS4X]] (+0.81, fdr 7e-06), [[RPL13A]] (+0.81, fdr 7e-06); moves opposite to [[LARP7]] (-0.63, fdr 3e-05), [[LZIC]] (-0.61, fdr 4e-05), [[ZNF518A]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8495.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +9.5 | 2e-18 | 35/37 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.59×** | +9.3 | 3e-18 | 42/45 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +6.1 | 3e-07 | 34/45 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +5.7 | 1e-06 | 36/45 (J82, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.003 | 30/48 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.008 | 25/48 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.8 | 0.012 | 30/46 (SW1417, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.45×** | +3.6 | 0.026 | 25/46 (NCI-H460, A-172, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.026 | 28/48 (J82, HT-29, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8495.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.464×** | -9.8 | 7e-20 | 43/47 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.853× | -5.1 | 1e-04 | 13/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -4.3 | 0.004 | 30/47 (C-33 A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.693×** | -3.4 | 0.097 | 24/48 (AsPC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 62.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -8.9) |
| [[C-33 A (line)]] | alt | 47.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -15.7) |
| [[LS 180 (line)]] | wt | 50.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 48.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 36.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.9) |
| [[A-172 (line)]] | wt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 36.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -15.7) |
| [[A549 (line)]] | wt | 30.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 31.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 51.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -8.7) |
| [[HT-29 (line)]] | alt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.1) |
| [[J82 (line)]] | alt | 27.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.7) |
| [[KATO III (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 41.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -9.3) |
| [[PANC-1 (line)]] | alt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.4) |
| [[SHP-77 (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 36.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 43.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.8) |
| [[A498 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1G]] | +0.87 | +0.89 / +0.82 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 889 |
| [[RPS4X]] | +0.81 | +0.78 / +0.80 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPL13A]] | +0.81 | +0.82 / +0.78 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7]] | +0.80 | +0.80 / +0.77 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL27A]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS20]] | +0.78 | +0.76 / +0.76 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL39]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPS18]] | +0.77 | +0.86 / +0.64 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS15A]] | +0.76 | +0.77 / +0.70 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 998 |
| [[RPLP0]] | +0.76 | +0.78 / +0.68 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RACK1]] | +0.76 | +0.80 / +0.71 | both halves | 7e-06 | STRING 999 |
| [[RPL14]] | +0.75 | +0.69 / +0.74 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP7]] | -0.63 | -0.69 / -0.44 | both halves | 3e-05 | STRING 543 |
| [[LZIC]] | -0.61 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[ZNF518A]] | -0.61 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[MIS12]] | -0.58 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[SLC35A4]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.56 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[ZNF764]] | -0.55 | -0.64 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.0, -29.8); signed map (-61.1, -6.4). **Vector** length 73.2, 19.5% of its response variance represented; |z| ≥ 3 in 501 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.60 to 19); *Translation initiation complex formation* (reactome, mean cos +0.59 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.59 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +2.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +4.2 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.7 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.8 | +0.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | -0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.0 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.0 | +0.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.6 | -0.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.6 | -0.4 |
|  | [[Thymol (drug)]] 5 µM |  | -1.3 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:51,993,522-51,995,895 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HIP, HUMRPL29, L29, eL29; previously RPL29P10 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P47914](https://www.uniprot.org/uniprotkb/P47914) (Large ribosomal subunit protein eL29):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6159](https://www.ncbi.nlm.nih.gov/gene/6159):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a cytoplasmic ribosomal protein that is a component of the 60S subunit. The protein belongs to the L29E family of ribosomal proteins. The protein is also a peripheral membrane protein expressed on the cell surface that directly binds heparin. Although this …

**Accessions** — [HGNC:10331](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10331) · Entrez [6159](https://www.ncbi.nlm.nih.gov/gene/6159) · UniProt [P47914](https://www.uniprot.org/uniprotkb/P47914) · Ensembl [ENSG00000162244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162244)

## Data

Gene col 8495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8495); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8495]; `tensor/DDL_lfc|DDL_z.npy` [8495]; `embed/gene_vectors.npy` [8495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8495 or target_col == 8495). Every well: [[RPL29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
