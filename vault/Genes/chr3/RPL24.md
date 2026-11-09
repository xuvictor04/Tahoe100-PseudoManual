---
symbol: "RPL24"
type: "gene"
col: 3548
ensembl_id: "ENSG00000114391"
name: "ribosomal protein L24"
location: "3q12.3"
module: 43
arm: "+"
pooled_cpm: 195.71
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL24

*ribosomal protein L24* — 3q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.62× (z +7.5, q 3e-11, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +3.3, q 0.083, up in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H460 3.99×, SW480 3.33×, LoVo 3.41×, A549 3.72×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 3.45×, NCI-H460 3.82×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.31×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.416×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL37]] (+0.91, fdr 7e-06, ⚠ RPL37 in the vector space only through flagged drug-doses), [[RPL32]] (+0.91, fdr 7e-06), [[RPL15]] (+0.91, fdr 7e-06), [[RPL19]] (+0.90, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3548.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H460 3.99×, SW480 3.33×, LoVo 3.41×, A549 3.72×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 3.45×, NCI-H460 3.82×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.31×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.62×** | +7.5 | 3e-11 | 48/49 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.24×** | +6.1 | 3e-07 | 42/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.03×** | +4.8 | 2e-04 | 39/45 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.83×** | +4.7 | 3e-04 | 46/48 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.4 | 0.069 | 36/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.55×** | +3.3 | 0.083 | 39/47 (COLO 205, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.083 | 36/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | 1.50× | +3.2 | 0.11 | 35/48 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.416×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 260 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 153 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 200 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[C-33 A (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 181 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 282 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 225 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 183 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 900 (line)]] | alt | 154 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 173 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 286 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 222 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 195 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 247 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 177 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 217 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 171 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 181 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 283 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 209 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 313 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 191 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 268 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL37]] ⚠ | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL32]] | +0.91 | +0.82 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL15]] | +0.91 | +0.81 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.90 | +0.82 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS10]] | +0.89 | +0.78 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.89 | +0.77 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS13]] ⚠ | +0.89 | +0.78 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL26]] | +0.88 | +0.75 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.88 | +0.78 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.88 | +0.76 / +0.90 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.88 | +0.75 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.87 | +0.71 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.87 | +0.72 / +0.90 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL28]] | +0.87 | +0.72 / +0.91 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL5]] | +0.87 | +0.81 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.892). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.6, -27.9); signed map (-61.6, -4.1). **Vector** length 73.9, 38.7% of its response variance represented; |z| ≥ 3 in 496 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.75 to 19); *Translation initiation complex formation* (reactome, mean cos +0.73 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.73 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +0.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.8 | -0.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -5.1 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -5.0 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -4.8 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.6 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +0.5 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -0.3 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.4 | +0.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.4 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.3 — chr3:101,681,091-101,686,733 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L24, eL24 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P83731](https://www.uniprot.org/uniprotkb/P83731) (Large ribosomal subunit protein eL24):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6152](https://www.ncbi.nlm.nih.gov/gene/6152):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L24E family of ribosomal proteins. It is located in the cytoplasm. This gene has been referred to as ribosomal protein L30 because the encoded protein shares amino acid …

**Accessions** — [HGNC:10325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10325) · Entrez [6152](https://www.ncbi.nlm.nih.gov/gene/6152) · UniProt [P83731](https://www.uniprot.org/uniprotkb/P83731) · Ensembl [ENSG00000114391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114391)

## Data

Gene col 3548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3548); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3548]; `tensor/DDL_lfc|DDL_z.npy` [3548]; `embed/gene_vectors.npy` [3548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3548 or target_col == 3548). Every well: [[RPL24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
