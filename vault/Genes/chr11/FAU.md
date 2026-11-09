---
symbol: "FAU"
type: "gene"
col: 7411
ensembl_id: "ENSG00000149806"
name: "FAU ubiquitin like and ribosomal protein S30 fusion"
location: "11q13.1"
module: 131
arm: "+"
pooled_cpm: 95.95
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# FAU

*FAU ubiquitin like and ribosomal protein S30 fusion* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.43× (z +6.7, q 9e-09, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +4.3, q 0.002, up in 38 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 4.98×, NCI-H460 5.14×, NCI-H1573 6.12×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.339×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS13]] (+0.91, fdr 7e-06, ⚠ RPS13 in the vector space only through flagged drug-doses), [[RPS29]] (+0.88, fdr 7e-06), [[RPL28]] (+0.88, fdr 7e-06), [[RPL15]] (+0.87, fdr 7e-06); moves opposite to [[PNPO]] (-0.66, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7411.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 4.98×, NCI-H460 5.14×, NCI-H1573 6.12×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.43×** | +6.7 | 9e-09 | 46/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.68×** | +5.8 | 2e-06 | 41/43 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.25×** | +5.2 | 3e-05 | 48/48 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.10×** | +4.8 | 2e-04 | 42/48 (SW 900, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.16×** | +4.6 | 4e-04 | 43/45 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +4.5 | 8e-04 | 44/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.3 | 0.002 | 38/49 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.62× | +3.1 | 0.12 | 38/48 (SW480, A-172, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7411.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.339×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.700× | -3.2 | 0.67 | 45/48 (KATO III, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 74.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 62.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[RKO (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 80.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 100.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 143 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 149 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 93.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 24 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS13]] ⚠ | +0.91 | +0.84 / +0.92 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS29]] | +0.88 | +0.74 / +0.92 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL28]] | +0.88 | +0.73 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS15]] ⚠ | +0.88 | +0.74 / +0.92 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL15]] | +0.87 | +0.81 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP2]] | +0.85 | +0.72 / +0.89 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS16]] ⚠ | +0.85 | +0.81 / +0.85 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS11]] | +0.84 | +0.65 / +0.89 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL36A]] | +0.84 | +0.74 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27A]] ⚠ | +0.84 | +0.78 / +0.83 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS25]] | +0.83 | +0.69 / +0.89 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL8]] ⚠ | +0.83 | +0.71 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL32]] | +0.83 | +0.69 / +0.86 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7A]] | +0.82 | +0.66 / +0.87 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS10]] | +0.82 | +0.68 / +0.86 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS21]] | +0.82 | +0.61 / +0.90 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS23]] | +0.82 | +0.62 / +0.88 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.66 | -0.50 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.898). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-47.2, -26.7); signed map (-61.8, -2.8). **Vector** length 68.9, 33.7% of its response variance represented; |z| ≥ 3 in 488 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.84 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.9 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.9 | +0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +1.8 | +5.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.6 |
|  | [[Rapamycin (drug)]] 0.05 µM |  | +1.5 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.5 | -0.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -5.7 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -5.7 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -5.5 | +5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | +0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | FAU ubiquitin like and ribosomal protein S30 fusion |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,120,630-65,122,177 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPS30, FLJ22986, Fub1, Fubi, MNSFbeta, asr1, S30, eS30 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62861](https://www.uniprot.org/uniprotkb/P62861) (Ubiquitin-like FUBI-ribosomal protein eS30 fusion protein):

> [Ubiquitin-like protein FUBI]: May have pro-apoptotic activity.; [Small ribosomal subunit protein eS30]: Component of the 40S subunit of the ribosome. Contributes to the assembly and function of 40S ribosomal subunits.

**Summary**, from NCBI Gene [2197](https://www.ncbi.nlm.nih.gov/gene/2197):

> This gene is the cellular homolog of the fox sequence in the Finkel-Biskis-Reilly murine sarcoma virus (FBR-MuSV). It encodes a fusion protein consisting of the ubiquitin-like protein fubi at the N terminus and ribosomal protein S30 at the C terminus. It has been proposed that the fusion protein is post-translationally processed to generate free fubi and free ribosomal protein S30. Fubi is a member of the ubiquitin family, and ribosomal protein S30 belongs to the S30E family of ribosomal …

**Accessions** — [HGNC:3597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3597) · Entrez [2197](https://www.ncbi.nlm.nih.gov/gene/2197) · UniProt [P62861](https://www.uniprot.org/uniprotkb/P62861) · Ensembl [ENSG00000149806](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149806)

## Data

Gene col 7411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7411); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7411]; `tensor/DDL_lfc|DDL_z.npy` [7411]; `embed/gene_vectors.npy` [7411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7411 or target_col == 7411). Every well: [[FAU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
