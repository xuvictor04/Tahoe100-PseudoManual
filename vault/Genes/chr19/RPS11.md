---
symbol: "RPS11"
type: "gene"
col: 6628
ensembl_id: "ENSG00000142534"
name: "ribosomal protein S11"
location: "19q13.3"
module: 131
arm: "+"
pooled_cpm: 198.77
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPS11

*ribosomal protein S11* — 19q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.85× (z +7.9, q 1e-12, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SHP-77 4.99×, SW480 4.68×, C32 5.51×, LoVo 4.71×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.530× (z -5.8, q 4e-06, down in 45 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (C-33 A 0.328×, NCI-H661 0.197×, AN3 CA 0.303×, SW480 0.355×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS23]] (+0.95, fdr 7e-06), [[RPL28]] (+0.95, fdr 7e-06), [[RPL32]] (+0.94, fdr 7e-06); moves opposite to [[DCLRE1A]] (-0.67, fdr 7e-06), [[SLC35A4]] (-0.67, fdr 7e-06), [[EIF4G1]] (-0.66, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6628.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SHP-77 4.99×, SW480 4.68×, C32 5.51×, LoVo 4.71×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.85×** | +7.9 | 1e-12 | 49/49 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +6.5 | 2e-08 | 42/44 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **2.10×** | +4.7 | 4e-04 | 47/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +4.4 | 0.001 | 42/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.43× | +3.2 | 0.12 | 31/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | 1.66× | +3.2 | 0.12 | 40/48 (NCI-H460, LoVo, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 2.48× | +3.1 | 0.14 | 45/48 (HCT15, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.71× | +3.1 | 0.14 | 36/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6628.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (C-33 A 0.328×, NCI-H661 0.197×, AN3 CA 0.303×, SW480 0.355×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.530×** | -5.8 | 4e-06 | 45/48 (C-33 A, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.624× | -3.0 | 0.68 | 33/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6628. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 223 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.1) |
| [[AN3 CA (line)]] | alt | 285 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.1) |
| [[C-33 A (line)]] | alt | 292 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.0) |
| [[C32 (line)]] | wt | 106 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 225 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -8.7) |
| [[LoVo (line)]] | wt | 358 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 225 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -8.5) |
| [[SHP-77 (line)]] | alt | 144 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 182 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 267 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 204 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 237 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 264 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 195 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 178 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 226 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 379 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 182 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 221 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 209 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 242 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 177 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 230 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 233 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 233 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6628), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS23]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL28]] | +0.95 | +0.93 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.94 | +0.94 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL38]] | +0.93 | +0.89 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS21]] | +0.92 | +0.92 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS25]] | +0.91 | +0.89 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS29]] | +0.91 | +0.88 / +0.91 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL8]] ⚠ | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS13]] ⚠ | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPLP2]] | +0.90 | +0.88 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS15]] ⚠ | +0.90 | +0.85 / +0.89 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS10]] | +0.89 | +0.90 / +0.88 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL7A]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL15]] | +0.88 | +0.78 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36A]] | +0.88 | +0.84 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1A]] | -0.67 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[SLC35A4]] | -0.67 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.66 | -0.61 / -0.65 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 891 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.951). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-47.2, -27.2); signed map (-61.8, -3.2). **Vector** length 86.3, 53.8% of its response variance represented; |z| ≥ 3 in 396 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.91 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +0.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.3 | +2.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | -0.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | +0.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.6 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.9 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.3 — chr19:49,496,365-49,499,708 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S11, uS17 |
| Gene groups (HGNC) | S ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62280](https://www.uniprot.org/uniprotkb/P62280) (Small ribosomal subunit protein uS17):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [6205](https://www.ncbi.nlm.nih.gov/gene/6205):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a member of the S17P family of ribosomal proteins that is a component of the 40S subunit. This gene is co-transcribed with the small nucleolar RNA gene U35B, which is located in the third intron. As is typical for genes encoding ribosomal proteins, there are …

**Accessions** — [HGNC:10384](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10384) · Entrez [6205](https://www.ncbi.nlm.nih.gov/gene/6205) · UniProt [P62280](https://www.uniprot.org/uniprotkb/P62280) · Ensembl [ENSG00000142534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142534)

## Data

Gene col 6628: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6628); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6628, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6628]; `tensor/DDL_lfc|DDL_z.npy` [6628]; `embed/gene_vectors.npy` [6628]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6628 or target_col == 6628). Every well: [[RPS11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
